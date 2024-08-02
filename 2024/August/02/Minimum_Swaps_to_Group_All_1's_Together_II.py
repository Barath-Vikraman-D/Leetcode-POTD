#! /usr/bin/env python3

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        swaps,n = 0,len(nums)
        total_ones = sum(nums)
        current_ones = sum(nums[:total_ones])
        swaps = total_ones-current_ones
        for i in range(total_ones,n+total_ones):
            current_ones+=-nums[i-total_ones]+nums[i%n]
            swaps = min(swaps,total_ones-current_ones)
        return swaps
