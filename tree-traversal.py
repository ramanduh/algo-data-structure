#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversalIter(self, root: TreeNode) -> List[int]:
        curr = root
        res = []
        stack = []

        while True:
            if curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                curr = curr.right
            else:
                break
        return res

    def preorderTraversalRec(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) \
            + self.preorderTraversal(root.right)

    def inorderTraversalRec(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] \
            + self.inorderTraversal(root.right)

    def inorderTraversalIter(self, root: TreeNode) -> List[int]:
        curr = root
        stack = []
        res = []

        while True:
            if curr:
                # Go on the most left
                stack.append(curr)
                curr = curr.left
            elif stack:
                # Process the current then go to the right
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            else:
                break
        return res

    def postorderTraversalIter(self, root):

        def peak(stack):
            if stack:
                return stack[-1]
            else:
                return None

        stack = []
        res = []
        curr = root

        if not curr:
            return []

        while curr or stack:
            while curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if curr.right and curr.right == peak(stack):
                tmp = curr
                curr = stack.pop()
                stack.append(tmp)
            else:
                res.append(curr.val)
                curr = None

        return res

    def postorderTraversalRec(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) \
            + self.postorderTraversal(root.right) \
            + [root.val]

    def leverOrderIter(self, root):
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            res.append([n.val for n in queue])
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp

        return res

    def levelOrderRec(self, root):
        levels = collections.defaultdict(list)

        def helper(root, level):
            if not root:
                return
            levels[level].append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)

        if not root:
            return []
        helper(root, 0)
        return levels.values()
