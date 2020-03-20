#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


class BruteForce:
    def search(self, S, sub):
        '''
        O(m*n)
        '''
        for i in range(len(S)-len(sub)+1):
            for j in range(len(sub)):
                if sub[j] != S[i+j]:
                    break
            else:
                return True

        return False


class RabinKarp:
    FP = 128  # fingerprint

    def hash(self, word):
        """
        reverse word in base FP
        """
        res = 0
        for i in range(len(word)):
            res += ord(word[i]) * (RabinKarp.FP**i)
        return res

    def search(self, S, sub):
        '''
        O(m+n)
        '''
        # Fill rolling hashes: O(m)
        hashes = [0] * (len(S) - len(sub) + 1)

        hashes[0] = self.hash(S[0:len(sub)])

        for i in range(1, len(hashes)):
            hashes[i] = hashes[i-1] - ord(S[i-1])
            hashes[i] /= RabinKarp.FP
            hashes[i] += ord(S[i+len(sub)-1]) * (RabinKarp.FP**(len(sub)-1))

        # Compare: O(m+n)
        target_hash = self.hash(sub)
        for i in range(len(hashes)):
            if hashes[i] == target_hash:
                for k in range(len(sub)):
                    if S[k+i] != sub[k]:
                        break
                else:
                    return True

        return False


class KMP:
    def search(self, S, sub):
        '''
        O(m+n)
        '''
        pass


class ZAlgorithm:
    def computeZ(self, S):
        """https://www.youtube.com/watch?v=CpZh4eF8QBw"""
        N = len(S)
        res = [0] * N
        left, right = 0, 0

        for k in range(1, N):
            if k > right:
                left = right = k
                while right < N and S[right] == S[right-left]:
                    right += 1
                res[k] = right - left
                right -= 1
            else:
                k1 = k - left
                if res[k1] < right-k+1:
                    res[k] = res[k1]
                else:
                    left = k
                    while right < N and S[right] == S[right-left]:
                        right += 1
                    res[k] = right - left
                    right -= 1

        return res

    def search(self, S, sub):
        '''
        O(m+n)
        '''
        newS = sub + '#' + S

        ztable = self.computeZ(newS)

        for count in ztable:
            if count == len(sub):
                return True
        return False


@pytest.mark.parametrize(
    'func',
    [
        BruteForce().search,
        RabinKarp().search,
        ZAlgorithm().search,
    ])
def test_search(func):
    assert func('abc', 'abc') is True
    assert func('hello', 'yo') is False
    assert func('algorithm is fun', 'fun') is True
