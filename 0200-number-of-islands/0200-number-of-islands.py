class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs_sink(r, c):
            is_out_of_bounds = r < 0 or r >= rows or c < 0 or c >= cols
            if is_out_of_bounds or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'            
            dfs_sink(r + 1, c)  # Down
            dfs_sink(r - 1, c)  # Up
            dfs_sink(r, c + 1)  # Right
            dfs_sink(r, c - 1)  # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs_sink(r, c)
        
        return island_count