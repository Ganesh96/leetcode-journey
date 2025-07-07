class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # Define the search space for the starting index of our k-element window.
        left = 0
        right = len(arr) - k

        # Binary search for the best starting position.
        while left < right:
            mid = (left + right) // 2
            
            # Compare the distance of the start of the window (arr[mid])
            # with the distance of the first element outside the window (arr[mid + k]).
            if x - arr[mid] > arr[mid + k] - x:
                # If the start element is further away, it means a better window
                # could exist to the right. Discard the left half.
                left = mid + 1
            else:
                # Otherwise, the current window is better or equal. Discard the right half,
                # but keep 'mid' as a potential best starting point.
                right = mid
        
        # The loop converges on the best starting index, which is `left`.
        # Return the k-sized slice starting from this index.
        return arr[left : left + k]