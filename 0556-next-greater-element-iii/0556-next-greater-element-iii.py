class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert the number to a list of character digits for manipulation.
        s = list(str(n))
        length = len(s)

        # Step 1: Find the pivot.
        # Iterate from the right to find the first digit (i) that is
        # smaller than the digit to its right (i+1).
        pivot_index = -1
        for i in range(length - 2, -1, -1):
            if s[i] < s[i+1]:
                pivot_index = i
                break
        
        # If no such pivot exists, the number is the largest permutation possible.
        if pivot_index == -1:
            return -1

        # Step 2: Find the successor to swap with the pivot.
        # Search from the right for the smallest digit larger than the pivot.
        for j in range(length - 1, pivot_index, -1):
            if s[j] > s[pivot_index]:
                # Step 3: Perform the swap.
                s[pivot_index], s[j] = s[j], s[pivot_index]
                break
        
        # Step 4: Reverse the suffix to the right of the pivot.
        # This makes the new number the smallest possible greater permutation.
        left, right = pivot_index + 1, length - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        # Convert back to an integer.
        result = int("".join(s))
        
        # Check if the result fits in a 32-bit integer.
        return result if result < 2**31 else -1