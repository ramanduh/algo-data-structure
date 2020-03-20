#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DoubleLinkedList:

    def __init__(self, val=None):
        self.val = val

        self.next = None
        self.prev = None
        # Return key when a node id deleted from cache,
        # so we can delete it in the dict as well
        self.key = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = DoubleLinkedList()  # Head allows to popleft
        self.tail = DoubleLinkedList()  # Tail allow to add
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    def _delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def _move_to_end(self, node):
        self._delete_node(node)
        self._add_node(node)

    def _popleft(self):
        """Pop left in the double linked list"""
        node = self.head.next
        ret = node.key
        self._delete_node(node)
        return ret

    def get(self, key: int) -> int:
        """ O(1)"""
        node = self.cache.get(key)
        if not node:
            return -1

        self._move_to_end(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        """ O(1) """
        if len(self.cache) == self.capacity and key not in self.cache:
            # Delete oldest
            k = self._popleft()
            del self.cache[k]

        # Update
        if key in self.cache:  # Update
            self.cache[key].val = value
            self._move_to_end(self.cache[key])

        else:
            node = DoubleLinkedList(value)
            node.key = key
            self._add_node(node)
            self.cache[key] = node
