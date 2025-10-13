class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_list = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            prereq_list[a].append(b)
        
        visiting = set()
        res = []

        def dfs(course):
            if course in visiting:
                return False
            
            if course not in prereq_list:
                return True

            visiting.add(course)

            for prereq in prereq_list[course]:
                if dfs(prereq)==False:
                    return False

            visiting.remove(course)
            res.append(course)
            del prereq_list[course]
            return True
        
        for course in range(numCourses):
            if dfs(course)==False:
                return []
        
        return res