class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the n x n matrix.
        # This involves swapping matrix[r][c] with matrix[c][r].
        # We only need to iterate through the upper triangle of the matrix to
        # avoid swapping elements back to their original place.
        for r in range(n):
        #     # The inner loop can start from 'r' to only touch each pair once.
            for c in range(r, n):
        #         # Perform the in-place swap.
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        
        # At this point, the matrix is transposed.
        # e.g., [[1,2,3],[4,5,6],[7,8,9]] has become [[1,4,7],[2,5,8],[3,6,9]]

        # Step 2: Reverse each row of the transposed matrix.
        # Iterate through each row in the matrix.
        for r in range(n):
            # Reverse the current row 'matrix[r]' in-place.
            # Most programming languages provide a built-in, in-place
            # function to reverse a list or array.
            matrix[r].reverse()
            
        # After this step, the rotation is complete. The function doesn't need to return anything.