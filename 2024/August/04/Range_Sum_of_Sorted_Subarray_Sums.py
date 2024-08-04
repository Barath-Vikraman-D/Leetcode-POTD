#! /usr/bin/env python3

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        hq = [(n,i) for i,n in enumerate(nums)]
        heapq.heapify(hq)
        for i in range(left-1):
            p,i = heapq.heappop(hq)
            if i+1<n:
                heapq.heappush(hq,(p+nums[i+1],i+1))
        for i in range(left-1,right):
            p,i = heapq.heappop(hq)
            if i+1<n:
                heapq.heappush(hq,(p+nums[i+1],i+1))
            res = (res %MOD + p % MOD) %MOD
        return res 
