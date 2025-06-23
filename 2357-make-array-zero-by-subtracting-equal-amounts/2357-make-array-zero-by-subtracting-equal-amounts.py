class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        
        # Step 1: Create a hash set to store unique positive numbers.
        unique_positives = set()
        
        # Step 2: Iterate through the input array.
        for num in nums:
            # If the number is positive, add it to the set.
            # The set will handle duplicates automatically.
            if num > 0:
                unique_positives.add(num)
        
        # Step 3: The answer is the number of elements in the set.
        return len(unique_positives)