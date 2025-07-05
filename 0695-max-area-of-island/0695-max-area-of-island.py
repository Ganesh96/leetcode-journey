class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs_get_area(r, c):
            
            is_out_of_bounds = r < 0 or r >= rows or c < 0 or c >= cols

            if is_out_of_bounds or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area = 1
            area += dfs_get_area(r + 1, c) # Down
            area += dfs_get_area(r - 1, c) # Up
            area += dfs_get_area(r, c + 1) # Right
            area += dfs_get_area(r, c - 1) # Left
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_island_area = dfs_get_area(r, c)

                    max_area = max(max_area, current_island_area)
        
        return max_area