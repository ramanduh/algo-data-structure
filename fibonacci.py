#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


def fib1(N):
    """
    Recursion

    Time complexity: O(2**N)
    Space complexity: O(2**N)
    """
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fib1(N-2) + fib1(N-1)


def fib2(N):
    """
    Recursion with memoization

    Time complexity: O(N)
    Space complexity: O(N)
    """

    def fib_helper(N, memo):
        if N == 0:
            return 0
        if N == 1:
            return 1

        if N not in memo:
            memo[N] = fib_helper(N-2, memo) + fib_helper(N-1, memo)

        return memo[N]

    return fib_helper(N, {})


def fib3(N):
    """
    Dynamic programing

    Time complexity: O(N)
    Space complexity: O(N)
    """
    res = [0, 1]

    for i in range(2, N + 1):
        res.append(res[i-1] + res[i-2])

    return res[N]


def fib4(N):
    """
    Dynamic programing

    Time complexity: O(N)
    Space complexity: O(1)
    """
    if N == 0:
        return 0

    a = 0
    b = 1
    c = 1

    for i in range(2, N + 1):
        c = a + b
        a = b
        b = c

    return c


@pytest.mark.parametrize('func', [fib1, fib2, fib3, fib4])
def test_fibonacci(func):
    assert func(0) == 0
    assert func(1) == 1
    assert func(2) == 1
    assert func(10) == 55


if __name__ == '__main__':
    import timeit
    print("Compute fibo of 10")
    print("Recursion time:")
    print(timeit.timeit(lambda: fib1(10)))
    print("Recursion with memoization time:")
    print(timeit.timeit(lambda: fib2(10)))
    print("Dynamic prog time:")
    print(timeit.timeit(lambda: fib3(10)))
    print("Dynamic programing space optimized time:")
    print(timeit.timeit(lambda: fib4(10)))
