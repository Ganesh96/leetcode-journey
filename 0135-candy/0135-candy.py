class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        # Step 1: Give each child 1 candy initially.
        candies = [1] * n

        # Step 2: Left-to-right pass to satisfy the 'left neighbor' rule.
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Step 3: Right-to-left pass to satisfy the 'right neighbor' rule.
        # This pass ensures that a child with a higher rating also gets more
        # than their right neighbor, without violating the left-side rule.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        # Step 4: The total number of candies is the sum of the array.
        return sum(candies)