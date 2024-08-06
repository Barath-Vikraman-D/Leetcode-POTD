#! /usr/bin/env python3

class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = Counter(word)
        heap = [-freq for freq in frequency.values()]
        heapq.heapify(heap)
        total_pushes,index=0,0
        while heap:
            total_pushes += (1+index//8)*(-heapq.heappop(heap))
            index += 1
        return total_pushes
