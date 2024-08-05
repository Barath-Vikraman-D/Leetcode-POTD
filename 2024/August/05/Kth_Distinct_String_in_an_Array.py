#! /usr/bin/env python3

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_map = defauldict(int)
        for ele in arr:
            hash_map[ele] += 1
        for ele in arr:
            if hash_map[ele] == 1:
                k -= 1
            if k == 0:
                return ele
        return ""
