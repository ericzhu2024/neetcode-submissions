class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            preMap[c].append(p)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)

            for p in preMap[course]:
                if not dfs(p):
                    return False
            
            preMap[course] = []
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True