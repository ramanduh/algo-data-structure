#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import heapq


"""
     6
A------------B
|           /| \
|          / |  \
|         /  |   \5
|        /   |    \
|1      /    |     \
|      /     |2     \
|     /2     |      /C
|    /       |     /
|   /        |    /
|  /         |   /5
| /          |  /
|/           | /
D------------E
      1

"""


def dijktra(P, N, src, dest):
    # Create an adjency list from P
    graph = collections.defaultdict(list)
    for s, d, w in P:
        graph[s].append((d, w))
        graph[d].append((s, w))

    # Hash table to keep shortest paths
    dists = {}

    queue = [(0, src)]  # Priority queue
    while queue:
        prev_w, node = heapq.heappop(queue)

        if node in dists:
            continue

        dists[node] = prev_w

        for d, w in graph[node]:
            if d not in dists:  # use dists to keep visited
                heapq.heappush(queue, (w+prev_w, d))

    return dists[dest]


def test_dijktra():
    P = [  # source, destination, weight
            ['A', 'B', 6],
            ['A', 'D', 1],
            ['B', 'D', 2],
            ['B', 'E', 2],
            ['D', 'E', 1],
            ['B', 'C', 5],
            ['E', 'C', 5],
        ]
    N = [chr(i) for i in range(ord('A'), ord('E')+1)]
    assert dijktra(P, N, 'A', 'C') == 7
