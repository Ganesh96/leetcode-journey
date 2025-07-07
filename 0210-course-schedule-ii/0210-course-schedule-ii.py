import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visiting = set()
        res = [0]

        def dfs(crs):
            if crs in visiting:
                return False
            
            if preMap[crs]==[]:
                return True
            visiting.add(crs)

            for neighbour in preMap[crs]:
                if not dfs(neighbour):
                    return False
            
            visiting.remove(crs)
            res.append(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res