class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        # Step 1: Ensure nums1 is the smaller array to optimize search space.
        if len(nums1) > len(nums2):
        #     # Swap the arrays if nums1 is larger.
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2
        
        # Step 2: Binary search for the partition in the smaller array (nums1).
        low, high = 0, m
        
        while low <= high:
            # partition1 is the cut point in nums1.
            partition1 = (low + high) // 2
            # partition2 is the corresponding cut point in nums2.
            partition2 = half_len - partition1
            
            # Step 3: Get the four boundary elements, handling edge cases
            # where a partition might be empty (0 elements) or contain all elements.
            
            max_left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            min_right1 = nums1[partition1] if partition1 < m else float('inf')
            
            max_left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            min_right2 = nums2[partition2] if partition2 < n else float('inf')
            
            # Step 4: Check if we have found the correct partition.
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                
                # --- This is the correct partition, calculate the median ---
                if total_len % 2 == 0: # Even number of elements
                    # median is avg of max of left parts and min of right parts
                    max_left = max(max_left1, max_left2)
                    min_right = min(min_right1, min_right2)
                    return (max_left + min_right) / 2.0
                else: # Odd number of elements
                    # median is the max of the left parts
                    return float(max(max_left1, max_left2))
            
            # Step 5: Adjust the search space if partition is incorrect.
            elif max_left1 > min_right2:
                # The partition in nums1 is too large. Move left.
                high = partition1 - 1
            else: # max_left2 > min_right1
                # The partition in nums1 is too small. Move right.
                low = partition1 + 1