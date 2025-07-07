class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Pre-calculate the total sums for original even/odd indices.
        total_even_sum = sum(nums[i] for i in range(0, n, 2))
        total_odd_sum = sum(nums[i] for i in range(1, n, 2))
        
        # `left_even_sum` and `left_odd_sum` will store the sums of elements
        # to the left of the current index `i`.
        left_even_sum = 0
        left_odd_sum = 0
        fair_indices_count = 0

        # Step 2: Iterate through the array to check each removal.
        for i in range(n):
            # The right sums are the totals minus the left sums and the current element.
            if i % 2 == 0: # Current element is at an even index
                right_even_sum = total_even_sum - left_even_sum - nums[i]
                right_odd_sum = total_odd_sum - left_odd_sum
            else: # Current element is at an odd index
                right_even_sum = total_even_sum - left_even_sum
                right_odd_sum = total_odd_sum - left_odd_sum - nums[i]
            
            # When nums[i] is removed, the right side's parity flips.
            new_even_sum = left_even_sum + right_odd_sum
            new_odd_sum = left_odd_sum + right_even_sum

            if new_even_sum == new_odd_sum:
                fair_indices_count += 1
            
            # Update the left sums for the next iteration.
            if i % 2 == 0:
                left_even_sum += nums[i]
            else:
                left_odd_sum += nums[i]

        return fair_indices_count