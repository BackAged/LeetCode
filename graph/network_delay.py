"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
"""

from queue import PriorityQueue
from math import inf
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        N = N + 1
        graph = [[] for i in range(N)]
        
        for [u, v, w] in times:
            graph[u].append((v, w))
        
        distance = [inf] * N
        distance[K] = 0

        visited = [False] * N
        visited[0] = True
        
        q = PriorityQueue()
        
        q.put((0, K))

        while not q.empty():
            _, s = q.get()
            # print(list(q.queue))

            if visited[s]:
                continue
            visited[s] = True
            
            for v, w in graph[s]:
                if  distance[s] + w < distance[v]:
                    distance[v] = distance[s] + w
                    q.put((distance[v], v))

        if False in visited:
            return -1

        return max(distance[1:])

print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3 , 1))