class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        # Step 1: Initialize the necessary data structures.
        # The answer array should be the same size and initialized to 0.
        # The stack will store indices of the days.
        n = len(temperatures)
        answer = [0] * n
        stack = []

        # Step 2: Iterate through the temperatures array with their indices.
        for current_day, current_temp in enumerate(temperatures):
            
            # Step 2a: Check if the current temperature can resolve any waiting days.
            # We look at the day on top of the stack. If the current day is warmer,
            # we've found the answer for that stacked day.
            # Keep checking as long as the stack has items AND the current day is warmer.
            while stack and current_temp > temperatures[stack[-1]]:
                
                # If it's warmer, pop the index of the previous, colder day.
                prev_day_index = stack.pop()
                
                # Calculate the number of days waited and update the answer array.
                answer[prev_day_index] = current_day - prev_day_index
            
            # Step 2b: After resolving all possible past days, add the current
            # day's index to the stack. It is now on the "waiting list".
            stack.append(current_day)
            
        # Step 3: Return the answer array. Any indices remaining on the stack
        # never found a warmer day, and their answer is correctly left as 0.
        return answer