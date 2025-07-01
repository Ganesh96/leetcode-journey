class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        
        # Step 1: Initialize variables.
        # `max_area` will store our final result.
        # `stack` will store pairs of (index, height) for bars in increasing height order.
        max_area = 0
        stack = [] 

        # Step 2: Iterate through the heights. A trick is to add a 0 to the end.
        # This sentinel value ensures that all bars remaining in the stack will be processed.
        for i, h in enumerate(heights + [0]):
            start = i
            # Step 2a: This `while` loop is the core of the monotonic stack.
            # It runs when we find a bar `h` that is shorter than the bar
            # at the top of the stack.
            while stack and h < stack[-1][1]:
                
                # Pop the bar from the stack. We now calculate the max area
                # for this popped bar.
                popped_index, popped_height = stack.pop()

                # Update the max area.
                max_area = max(max_area, popped_height * (i-popped_index))

                start = popped_index

            # Step 2b: Push the current bar's (index, height) onto the stack.
            # The stack maintains its increasing-height property.
            stack.append((start, h))
            
        # Step 3: Return the maximum area found.
        # The loop with the sentinel value handles all calculations, so we just return.
        return max_area