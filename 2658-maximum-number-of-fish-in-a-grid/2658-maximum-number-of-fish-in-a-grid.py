class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c,collected):
            if not(0<=r<rows and 0<=c<cols):
                return 0
            
            if grid[r][c]==0:
                return 0
            collected += grid[r][c]
            grid[r][c] = 0
            collected = max(dfs(r-1,c,collected), collected) # up
            collected = max(dfs(r+1,c,collected), collected) # down
            collected = max(dfs(r,c-1,collected), collected) # left
            collected = max(dfs(r,c+1,collected), collected) # right
            return collected

        max_fishes = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0:
                    fishes = dfs(i,j,0)
                    max_fishes = fishes if fishes> max_fishes else max_fishes
        return max_fishes