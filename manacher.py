#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find the longest palindrome by using manacher algo
"""


def expand(S, idx, start):
    count = start
    left = idx - start
    right = idx + start

    while left >= 0 and right < len(S):
        if S[left] == S[right]:
            count += 1
        else:
            break
        left -= 1
        right += 1

    return left + 1, right - 1, count - 1


def manacher(S):
    # man len(S) a odd number
    tmp = '#'
    for char in S:
        tmp += char + '#'
    S = tmp

    center = 0
    P = [0] * len(S)
    left = right = 0

    for i in range(len(S)):
        if i > left and i < right:
            # min(P[i'], right - i)
            start = min(P[center - (i - center)], right - i)
            l, r, count = expand(S, i, start)
            if r > right:
                right = r
                left = l
                center = i
            P[i] = count
        else:
            left, right, count = expand(S, i, 0)
            P[i] = count
            center = i

    return int((max(P) * 2 + 1) / 2)


def test_manacher():
    assert manacher("abba") == 4
    assert manacher("babad") == 3
    assert manacher("abacabacabb") == 9


def test_expand():
    assert expand("babad", 1, 0) == (0, 2, 1)
    assert expand("babad", 2, 0) == (1, 3, 1)
    assert expand("kayak", 2, 1) == (0, 4, 2)
    assert expand("kayak", 3, 0) == (3, 3, 0)
