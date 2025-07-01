import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        # Step 1: Build the graph from prerequisites.
        # Edge is prereq -> course.
        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Step 2: Initialize data structures.
        # `result_order` will store our topological sort in reverse post-order.
        # `visiting` and `visited` are for cycle detection, same as before.
        result_order = []
        visiting = set()
        visited = set()
        
        # --- DFS Helper Function ---
        # Returns True if acyclic, False if a cycle is found.
        def dfs(course):
            # Base Case 1: Cycle detected. Node is already in our current path.
            if course in visiting:
                return False
            
            # Base Case 2: Node already processed and confirmed safe.
            if course in visited:
                return True

            # Add node to the current path.
            visiting.add(course)

            # Recursively explore all neighbors.
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False # Propagate cycle detection
            
            # Backtrack and mark as fully visited.
            visiting.remove(course)
            visited.add(course)
            
            # --- THIS IS THE NEW STEP FOR TOPOLOGICAL SORT ---
            # Add the course to our result only AFTER all its neighbors are explored.
            # This is the post-order step.
            result_order.append(course)
            
            return True

        # --- Main Loop ---
        # Step 3: Run DFS from every potential starting node.
        for c in range(numCourses):
        #     # We check `c not in visited` as an optimization.
            if c not in visited:
                if not dfs(c):
        #             # If a cycle is detected at any point, a solution is impossible.
                    return []
        
        # Step 4: If the loop completes, a valid order exists.
        # The result_order is a post-order traversal. The topological sort
        # is the reverse of that.
        return result_order