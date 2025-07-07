import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # Step 1: Build an adjacency list to represent the graph.
        # The map is {prereq: [courses that need this prereq]}.
        # For a pair [a, b], the edge is b -> a.
        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Step 2: Create sets to track the state of each node.
        # `visiting`: Tracks nodes in the current DFS path to detect cycles.
        # `visited`: Tracks nodes that have been fully explored and are known to be safe.
        visiting = set()
        visited = set()
        
        # --- DFS Helper Function ---
        # Returns True if the path starting from `course` is acyclic, False otherwise.
        def dfs(course):
            # Base Case 1: A cycle is detected.
            # If we visit a node that is already in our current recursion path,
            # we've found a back-edge, which means there's a cycle.
            if course in visiting:
                return False
            
            # Base Case 2: This node has already been processed and is safe.
            # If we've already fully explored this node, we don't need to do it again.
            if course in visited:
                return True

            # Mark the current node as part of our active exploration path.
            visiting.add(course)

            # Explore all neighbors recursively.
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False # Propagate failure if a cycle is found downstream.
            
            # This path is safe. Backtrack and mark as fully visited.
            visiting.remove(course)
            visited.add(course)
            
            return True

        # --- Main Loop ---
        # Step 3: We must run DFS from every course in case the graph is not fully connected.
        for c in range(numCourses):
            if not dfs(c):
        #         # If any starting path leads to a cycle, we cannot finish.
                return False
        
        # If all paths are explored without finding a cycle, it's possible.
        return True