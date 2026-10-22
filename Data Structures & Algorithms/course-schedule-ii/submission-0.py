class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited, cycle = set(),set()
        preMap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res