class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])


        def dfs(r,c,a):
            if not (0<=r<rows and 0<=c<cols):
                return 0
            if(grid[r][c]!=1):
                return 0
            
            grid[r][c]=2
            a = max(a,dfs(r+1,c,a+1)) # up
            a = max(a,dfs(r-1,c,a+1)) # down
            a = max(a,dfs(r,c-1,a+1)) # left
            a = max(a,dfs(r,c+1,a+1)) # right

            return a
        
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area = dfs(i,j,1)
                    max_area = area if area > max_area else max_area
        return max_area
                