from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zeroes, extras = [],[]

        def compute(grid,zeroes,extras,zeroes_index)->int:
            L = len(extras)
            O = len(zeroes)
            if zeroes_index==O:
                return 0
            x,y = zeroes[zeroes_index]
            dist = 10**7
            for extra_index in range(L):
                dx,dy = extras[extra_index]
                if grid[dx][dy]>1:
                    grid[dx][dy]-=1
                    grid[x][y]=1
                    dist = min(dist, (abs(x-dx)+abs(y-dy)+compute(grid,zeroes,extras,zeroes_index+1)))
                    grid[dx][dy]+=1
                    grid[x][y]=0
            return dist


        for i in (0,1,2):
            for j in (0,1,2):
                if grid[i][j]==0:
                    zeroes.append((i,j))
                elif grid[i][j]>1:
                    extras.append((i,j))
        
        zeroes_index = 0
        return compute(grid,zeroes,extras,zeroes_index)