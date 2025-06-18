import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        """
        Processes tasks based on availability and priority using a min-heap.
        """
        # Step 1: Augment tasks with their original index.
        # Format: (enqueueTime, processingTime, original_index)
        indexed_tasks = []
        for i, task in enumerate(tasks):
            indexed_tasks.append((task[0], task[1], i))
        
        # Sort tasks based on their enqueue time to process them chronologically.
        indexed_tasks.sort()
        
        # This will be our final result.
        res = []
        # The min_heap stores available tasks, prioritized by processing time then index.
        # Format in heap: (processingTime, original_index)
        min_heap = []
        
        current_time = 0  # Represents the current time of the CPU.
        task_index = 0    # Pointer to the next task in `indexed_tasks`.
        num_tasks = len(tasks)
        
        # Loop until all tasks have been processed and added to the result.
        while len(res) < num_tasks:
            # Step 3a: Add all tasks that have become available by `current_time`.
            while task_index < num_tasks and indexed_tasks[task_index][0] <= current_time:
                enqueue_time, processing_time, original_index = indexed_tasks[task_index]
                heapq.heappush(min_heap, (processing_time, original_index))
                task_index += 1
            
            # Step 3b: Decide what the CPU does next.
            if min_heap:
                # If there are tasks in the available pool, process the highest priority one.
                processing_time, original_index = heapq.heappop(min_heap)
                
                # Advance time by the duration of the processed task.
                current_time += processing_time
                # Record the task's index in our result order.
                res.append(original_index)
            elif task_index < num_tasks:
                # If the available pool is empty, the CPU is idle.
                # Jump the clock forward to the enqueue time of the next unseen task.
                current_time = indexed_tasks[task_index][0]
                
        return res