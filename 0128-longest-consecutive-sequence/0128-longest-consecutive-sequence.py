class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        # Step 1: Create a hash set from the input list for O(1) lookups.
        # This also conveniently handles duplicate numbers in the input.
        num_set = set(nums)
        
        # Step 2: Initialize a variable to track the longest streak found.
        longest_streak = 0

        # Step 3: Iterate through each number in our set.
        for num in num_set:
        
            # Step 3a: The key insight: only start counting if 'num' is the
            # beginning of a sequence. We know it's a beginning if `num - 1`
            # is NOT in the set.
            if (num - 1) not in num_set:
            
                # If we found a starting point, initialize variables for this sequence.
                current_streak = 1
                
                # Step 3b: Use a while loop to count the length of this sequence.
                # Keep checking for the next consecutive number in the set.
                while (num + current_streak) in num_set:
                    current_streak += 1
                
                # Step 3c: Once the sequence is finished, update our overall longest streak.
                longest_streak = max(longest_streak, current_streak)
                
        # Step 4: After checking all numbers, return the result.
        return longest_streak