#! /usr/bin/env python3

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        num,step,index = 0,1,0
        directions = ([0,1],[1,0],[0,-1],[-1,0])
        while num<rows*cols:
            for _ in range(2):
                for _ in range(step):
                    if 0<=rStart<rows and 0<=cStart<cols:
                        result.append([rStart,cStart])
                        num += 1
                    rStart += directions[index][0]
                    cStart += directions[index][1]
                index = (index+1)%4
            step += 1
        return result
