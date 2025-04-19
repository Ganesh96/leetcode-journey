class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        big_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i,j,area)->int:
            if not (0<=i<rows and 0<=j<cols):
                return area
            if grid[i][j]!=1:
                return area
            grid[i][j] = 2
            area+=1
            area = dfs(i,j+1,area)
            area = dfs(i+1,j,area)
            area = dfs(i,j-1,area)
            area = dfs(i-1,j,area)
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area = dfs(i,j,0)
                    big_area = max(big_area,area)
        return big_area