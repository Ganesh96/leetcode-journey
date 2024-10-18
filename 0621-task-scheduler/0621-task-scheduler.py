from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        task_counts = Counter(tasks)
        # Step 2: Find the maximum frequency
        max_freq = max(task_counts.values())
        # Step 3: Count how many tasks have the maximum frequency
        max_freq_tasks = list(task_counts.values()).count(max_freq)
        
        # Step 4: Calculate the minimum required intervals
        # Part (f_max - 1) represents the number of full cycles (A -> B -> idle).
        # max_freq_tasks represents how many tasks share that maximum frequency.
        intervals = (max_freq - 1) * (n + 1) + max_freq_tasks
        
        # Step 5: The result is the max between total tasks and calculated intervals
        return max(len(tasks), intervals)
