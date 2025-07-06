class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        N = len(grid)

        def get_neighbors(r, c):
            """Helper to get valid neighbors within the grid."""
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc
        
        def dfs_paint_and_measure(r, c, island_id):
            """Paints an island with its ID and returns its area."""
            if not (0 <= r < N and 0 <= c < N and grid[r][c] == 1):
                return 0
            
            grid[r][c] = island_id
            area = 1
            for nr, nc in get_neighbors(r, c):
                area += dfs_paint_and_measure(nr, nc, island_id)
            return area

        # --- Pass 1: Find, paint, and measure all islands ---
        island_id = 2  # Start IDs at 2 since 0 and 1 are used.
        island_areas = {0: 0} # map island_id -> area
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area = dfs_paint_and_measure(r, c, island_id)
                    island_areas[island_id] = area
                    island_id += 1

        # The max_area is initially the largest existing island, or 0 if no islands exist.
        max_area = max(island_areas.values())

        # --- Pass 2: Check all water cells ---
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    neighbor_islands = set(grid[nr][nc] for nr, nc in get_neighbors(r, c))
                    potential_area = 1 + sum(island_areas[iid] for iid in neighbor_islands)
                    max_area = max(max_area, potential_area)
        
        # If max_area is 0 at the end, it means the grid was all 0s.
        # But we can flip one 0 to a 1, so the answer is 1 (if n>0).
        # If the grid was all 1s, max_area would be n*n, which is correct.
        return max_area if max_area > 0 else 1