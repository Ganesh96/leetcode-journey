class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            if min(r,c)<0 or r == rows or c==cols or grid[r][c]==0:# or (r,c) in visit:
                return 0
            
            #visit.add((r,c))
            aux = grid[r][c]
            grid[r][c] = 0
            res= 0
            near = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in near:
                res = max(res,aux + dfs(r+dr,c+dc))
            #visit.remove((r,c))
            grid[r][c] = aux
            return res
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                visited = set()
                res = max(res,dfs(r,c))

        return res