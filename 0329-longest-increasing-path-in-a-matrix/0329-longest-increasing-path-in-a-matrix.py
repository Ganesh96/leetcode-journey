class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])
        # cache[r][c] will store the length of the LIP starting at (r, c)
        cache = [[0] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            # If we have already computed the result for this cell, return it.
            if cache[r][c] > 0:
                return cache[r][c]

            # The path starting at (r, c) is at least 1 (the cell itself).
            max_path = 1
            
            # Explore 4-directional neighbors.
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                # Check if neighbor is valid and has a strictly greater value.
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    matrix[nr][nc] > matrix[r][c]):
                    
                    # The path length is 1 (current cell) + longest path from neighbor.
                    path_from_neighbor = 1 + dfs(nr, nc)
                    max_path = max(max_path, path_from_neighbor)
            
            # Cache the result before returning.
            cache[r][c] = max_path
            return max_path

        # Call DFS for every cell to find the overall maximum path length.
        longest_path = 0
        for r in range(ROWS):
            for c in range(COLS):
                longest_path = max(longest_path, dfs(r, c))
        
        return longest_path