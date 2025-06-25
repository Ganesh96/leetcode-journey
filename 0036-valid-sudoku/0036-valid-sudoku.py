import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # Step 1: Initialize data structures to track seen numbers for all regions.
        # Using defaultdict(set) is very convenient here.
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        # Step 2: Iterate through every cell on the 9x9 board using its coordinates.
        for r in range(9):
            for c in range(9):
        #         # Get the value from the current cell.
                num = board[r][c]

                # Step 2a: We only care about filled cells, so skip dots.
                if num == '.':
                    continue

                # Step 2b: Calculate the index for the 3x3 sub-box.
                # This formula maps (r, c) to a unique box ID from 0 to 8.
                box_id = (r // 3) * 3 + (c // 3)

                # Step 2c: Check for duplicates in all three regions at once.
                # If the number is already in the set for its row, column, OR box,
                # then we have found a rule violation.
                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box_id]):
                    return False

                # Step 2d: If it's not a duplicate, record this number as "seen"
                # for the current row, column, and box.
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)

        # Step 3: If the entire board is processed without finding any violations,
        # the board is valid.
        return True