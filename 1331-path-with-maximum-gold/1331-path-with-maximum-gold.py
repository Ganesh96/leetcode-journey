class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c,visit):
            if min(r,c)<0 or r == rows or c==cols or grid[r][c]==0 or (r,c) in visit:
                return 0
            
            visit.add((r,c))
            gold_collected = 0
            near = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in near:
                gold_collected = max(gold_collected,grid[r][c] + dfs(r+dr,c+dc,visit))
            visit.remove((r,c))
            return gold_collected
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                visited = set()
                res = max(res,dfs(r,c,visited))

        return res