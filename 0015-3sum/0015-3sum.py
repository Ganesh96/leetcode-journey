class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # Step 1: Sort the input array.
        # This is essential for the two-pointer approach and for handling duplicates.
        nums.sort()
        
        # Step 2: Initialize a list to store the results.
        result = []
        
        # Step 3: Iterate through the array with a pointer 'i' for the first element.
        # We stop at len(nums) - 2 because we need at least two more elements for a triplet.
        for i in range(len(nums) - 2):
            
            # Step 3a: Skip positive numbers for the first element.
            # If the first element is positive, the sum can never be zero
            # since the array is sorted. This is a small optimization.
            if nums[i] > 0:
                break
            
            # Step 3b: Skip duplicate values for the first element.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 3c: Set up the 'left' and 'right' pointers.
            left = i + 1
            right = len(nums) - 1
            
            # Step 3d: Run the two-pointer search.
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
            #         # Move left pointer to increase the sum.
                    left += 1
                elif current_sum > 0:
            #         # Move right pointer to decrease the sum.
                    right -= 1
                else: # Found a triplet that sums to zero.
            #         # Add it to the result.
                    result.append([nums[i], nums[left], nums[right]])
                    
            #         # Step 3e: Skip duplicates for the second and third elements.
            #         # Move the left pointer forward as long as it's a duplicate.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
            #         # Move the right pointer backward as long as it's a duplicate.
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
            #         # Move pointers to the next unique elements.
                    left += 1
                    right -= 1
                        
        # Step 4: Return the final list of triplets.
        return result