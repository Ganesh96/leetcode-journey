class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a row with 1s, as there's only one way to reach
        # any cell in the first row (by moving right).
        row = [1] * n

        # Iterate through the grid's rows, starting from the second row.
        for i in range(1, m):
            # Iterate through the columns, starting from the second column.
            # print("------------")
            for j in range(1, n):
                # The number of paths to the current cell (i, j) is the sum of
                # paths from the cell above (row[j]) and the cell to the left (row[j-1]).
                row[j] = row[j] + row[j-1]
                # print(row)


        # The final answer is the value in the bottom-right corner.
        return row[n-1]