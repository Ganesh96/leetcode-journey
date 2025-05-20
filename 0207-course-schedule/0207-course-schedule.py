class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def dfs(course):
            # if visiting, we found a cycle
            if visited[course]==1:
                return False
            if visited[course]==2:
                return True
            
            visited[course] = 1  # mark as visiting

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 2  # mark as fully visited
            return True


        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return False
        return True
