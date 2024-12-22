from typing import List

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """
        Calculates the minimum moves to spread stones over a grid.
        """
        def solve(grid, zeros, extras, curr_index):
            if curr_index == len(zeros):
                return 0

            curr_zero_x, curr_zero_y = zeros[curr_index]
            ans = 1000000
            for i in range(len(extras)):
                curr_x, curr_y = extras[i]
                if grid[curr_x][curr_y] > 1:
                    # Do
                    grid[curr_x][curr_y] -= 1
                    grid[curr_zero_x][curr_zero_y] = 1
                    ans = min(ans, abs(curr_zero_x - curr_x) + abs(curr_zero_y - curr_y) +
                              solve(grid, zeros, extras, curr_index + 1))

                    # Undo
                    grid[curr_x][curr_y] += 1
                    grid[curr_zero_x][curr_zero_y] = 0
            return ans

        zeros = []
        extras = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                elif grid[i][j] > 1:
                    extras.append((i, j))

        return solve(grid, zeros, extras, 0)