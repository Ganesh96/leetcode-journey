class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        # Step 1: Handle the edge case of an empty input list.
        if not intervals:
            return []

        # Step 2: Sort the intervals based on their start time (the first element).
        # This is the most important step.
        intervals.sort(key=lambda x: x[0])
        
        # Step 3: Initialize a list to store our merged intervals.
        # Start it with the first interval from the sorted list.
        merged_intervals = [intervals[0]]
        
        # Step 4: Iterate through the sorted intervals, starting from the second one.
        for i in range(1, len(intervals)):
            # Get the last interval we added to our results.
            last_merged = merged_intervals[-1]
            # Get the current interval we are considering.
            current_interval = intervals[i]
            
            # Step 4a: Check if the current interval overlaps with the last merged one.
            if current_interval[0] <= last_merged[1]:
                # If they overlap, we merge them by updating the end of the last
                # merged interval. The new end is the maximum of the two ends.
                last_merged[1] = max(last_merged[1], current_interval[1])
            else:
                # Step 4b: If they don't overlap, the current interval starts
                # a new merged block. Add it to our list.
                merged_intervals.append(current_interval)
                
        # Step 5: Return the final list of merged intervals.
        return merged_intervals