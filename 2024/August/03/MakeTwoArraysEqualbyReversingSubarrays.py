#! /usr/bin/env python3

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return  Counter(target)==Counter(arr)
        '''
        count = defaultdict(int)
        for ele1,ele2 in zip(target,arr):
            count[ele1]+=1
            count[ele2]-=1
        for cnt in count:
            if count[cnt]:
                return False
        return True
        '''    
