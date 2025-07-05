class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        # parent[i] stores the parent of element i.
        parent = list(range(ROWS * COLS))
        # size[i] stores the size of the set where i is the root.
        size = [0] * (ROWS * COLS)
        max_area = 0

        # Initialize size for all land cells and find initial max_area.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    idx = r * COLS + c
                    size[idx] = 1
                    max_area = 1

        def find(i):
            """Finds the root parent of element i with path compression."""
            # Base case: if i is its own parent, then it's the root of the set.
            if parent[i] == i:
                return i
            
            # Recursively call find on the parent until the root is found.
            # The "path compression" happens on this line. As the recursion unwinds,
            # it sets the parent of every node on the path to point directly to the final root.
            parent[i] = find(parent[i])
            
            return parent[i]

        def union(i, j):
            """Unites the sets containing i and j using union by size."""
            # nonlocal max_area
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                # Union by making the larger set the parent.
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i # Ensure root_i is larger
                
                parent[root_j] = root_i
                size[root_i] += size[root_j]
                # Update the max area after a successful merge.
                # max_area = max(max_area, size[root_i])
        
        # Main loop to connect adjacent land cells.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    idx1 = r * COLS + c
                    # Check down and right neighbors to avoid double-counting.
                    for dr, dc in [(1, 0), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and 
                            grid[nr][nc] == 1):
                            idx2 = nr * COLS + nc
                            union(idx1, idx2)
        
        return max(size)