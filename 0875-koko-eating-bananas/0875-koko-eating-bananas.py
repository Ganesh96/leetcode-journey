import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        # Step 1: Define the search space for the eating speed, k.
        # The lowest possible speed is 1. The highest necessary speed is the largest pile.
        left = 1
        right = max(piles)
        
        # This will hold the best possible answer we've found so far.
        result = right

        # Step 2: Perform the binary search.
        while left <= right:
            # 'k' is the middle speed we are testing in the current range.
            k = (left + right) // 2
            
            # Step 2a: Calculate the total hours required to finish at speed 'k'.
            total_hours = 0
            for p in piles:
                # The time to eat a pile 'p' is ceil(p / k).
                # Using math.ceil is clean. An integer math equivalent is (p + k - 1) // k.
                total_hours += math.ceil(p / k)
            
            # Step 2b: Check if this speed is feasible.
            if total_hours <= h:
                # This speed works! It's a potential answer.
                # Let's record it and try for an even better (slower) speed.
                # So, we search in the left half of our range.
                result = k
                right = k - 1
            else:
                # This speed is too slow. Koko needs to eat faster.
                # We must search in the right half of our range.
                left = k + 1
        
        # Step 3: After the loop, result will hold the minimum feasible speed.
        return result