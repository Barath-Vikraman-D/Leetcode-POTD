#! /usr/bin/env python3

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        if rows<3 or cols<3 : return 0
        def isMagicSquare(row,col):
            seen,magicSum = 0,grid[row][col] + grid[row][col+1] + grid[row][col+2]
            for r in range(3):
                s = 0
                for c in range(3):
                    s+= grid[row+r][col+c]
                    if grid[row+r][col+c]<1 or grid[row+r][col+c]>9: return False
                    if seen&(1<<grid[row+r][col+c]) : return False
                    seen |= 1<<grid[row+r][col+c]
                if magicSum != s : return False
            for c in range(3):
                s = sum([grid[row+r][col+c] for r in range(3)])
                if magicSum != s : return False
            ltr,rtl = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2],grid[row+2][col] + grid[row+1][col+1] + grid[row][col+2]
            return magicSum == ltr and rtl == ltr
        return sum([isMagicSquare(row,col) for col in range(cols-2) for row in range(rows-2)])
