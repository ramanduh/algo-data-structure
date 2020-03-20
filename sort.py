#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import math
import pytest


class BubbleSort:
    """
    Time: O(n**2)
    Space: O(1)
    """
    def sort(self, N):
        j = len(N)
        while j > 0:
            # Iterate till j-1 because each iteration put the max at the end
            for i in range(j - 1):
                if N[i] > N[i + 1]:
                    N[i], N[i + 1] = N[i + 1], N[i]
            j -= 1
        return N


class SelectionSort:
    """
    Time: O(n**2)
    Space: O(1)
    """
    def min_idx(self, N):
        res = -1
        low = float('inf')
        for i in range(len(N)):
            if N[i] < low:
                low = N[i]
                res = i
        return res

    def sort(self, N):
        for i in range(len(N)):
            idx = self.min_idx(N[i:])
            N[i], N[idx + i] = N[idx + i], N[i]

        return N


class MergeSort:
    """
    Time: O(n*log(n))
    Space: O(1)
    """
    def merge(self, L1, L2):
        """
        Merge 2 sorted lists and return a sorted list
        O(min(L1,L2))
        """
        i, j = 0, 0
        res = []

        while i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                res.append(L1[i])
                i += 1
            else:
                res.append(L2[j])
                j += 1

        if i < len(L1):
            res.extend(L1[i:])
        if j < len(L2):
            res.extend(L2[j:])
        return res

    def sort(self, N):
        if len(N) <= 1:
            return N

        mid = len(N) // 2
        left = self.sort(N[:mid])
        right = self.sort(N[mid:])

        return self.merge(left, right)


class QuickSort:
    """
    Average time: O(n*log(n))
    Worst time: O(n**2)
    """
    def partition(self, N, left, right):
        """Rearrange N so all the element < pivot goes before the pivot"""
        pivot = N[right]  # Use the last element as a pivot
        for i in range(left, right):
            if N[i] <= pivot:
                N[i], N[left] = N[left], N[i]
                left += 1

        # swap the pivot at the end
        N[left], N[right] = N[right], N[left]

        return left

    def sort(self, N):
        """
        The sort is performed in place
        """
        def sortHelper(N, left, right):
            if left < right:
                pivot_idx = self.partition(N, left, right)
                sortHelper(N, left, pivot_idx - 1)
                sortHelper(N, pivot_idx + 1, right)

        sortHelper(N, 0, len(N) - 1)
        return N

    def sortBasic(self, N):
        """
        Not space optimized to illustrate the worst time.
        eg: if left list is empty each time
        (ie the pivot is not the median each time)
        """
        if len(N) <= 1:
            return N
        pivot = N[-1]
        left = []
        right = []
        for i in range(len(N) - 1):
            if N[i] < pivot:
                left.append(N[i])
            else:
                right.append(N[i])
        return self.sort(left) + [pivot] + self.sort(right)


class BucketSort:
    def __init__(self, bucket_nb, max_elem):
        self.bucket_nb = bucket_nb
        self.max_elem = max_elem
        self.divider = math.ceil((self.max_elem) + 1 / self.bucket_nb)

    def _to_idx(self, n):
        return math.floor(n / self.divider)

    def sort(self, N):
        res = []
        bucket = collections.defaultdict(list)
        for number in N:
            # add num in the bucket
            bucket[self._to_idx(number)].append(number)
        for i in range(self.bucket_nb):
            if bucket[i]:
                bucket[i].sort()  # could use insertion sort
                res.extend(bucket[i])
        return res


class RadixSort:
    def __init__(self):
        self.max_bits = 4  # Because the max val in N is 9: 1001 (4bits)
        self.bucket0 = collections.deque([])
        self.bucket1 = collections.deque([])

    def sort(self, N):
        res = collections.deque(N)
        mask = 1
        for bit in range(self.max_bits):  # 4 steps
            # Fill bucket
            while res:
                num = res.popleft()
                if num & mask:
                    self.bucket1.append(num)
                else:
                    self.bucket0.append(num)
            # Emptying buckets
            while self.bucket0:
                res.append(self.bucket0.popleft())
            while self.bucket1:
                res.append(self.bucket1.popleft())

            mask <<= 1

        return list(res)


class InsertSort:
    pass


class TestSort:
    funcs = [
        sortClass.sort
        for sortClass in [
            BubbleSort(),
            SelectionSort(),
            MergeSort(),
            QuickSort(),
            BucketSort(5, 9),
            RadixSort(),
            # InsertSort(),
        ]
    ]
    ids = [
        'BubbleSort',
        'SelectionSort',
        'MergeSort',
        'QuickSort',
        'BucketSort',
        'RadixSort',
        # 'InsertSort',
    ]

    @pytest.mark.parametrize('func', funcs, ids=ids)
    def test_sort(self, func):
        assert func([]) == []
        assert func([0]) == [0]
        assert func([5, 3, 7, 2, 6, 9, 4, 8, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestSelectionSort:
    def test_min_idx(self):
        min_idx = SelectionSort().min_idx
        assert min_idx([]) == -1
        assert min_idx([2]) == 0
        assert min_idx([5, 3, 2, 9, 4, 1]) == 5


class TestMergeSort:
    def test_merge(self):
        merge = MergeSort().merge
        assert merge([2, 3, 5], [1, 4, 9]) == [1, 2, 3, 4, 5, 9]
        assert merge([2], []) == [2]
        assert merge([2], [1, 3]) == [1, 2, 3]


class TestQuickSort:
    def test_partition(self):
        partition = QuickSort().partition
        N = [5, 3, 2, 9, 1, 4]
        assert partition(N, 0, 5) == 3  # index of the pivot
        assert N == [3, 2, 1, 4, 5, 9]
