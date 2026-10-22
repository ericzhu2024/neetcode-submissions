class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preMap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            preMap[c].append(p)
        visited = set()
        res = []
        def dfs(u, v):
            if u == v:
                return True
            if u in visited:
                return False
            visited.add(u)
            for p in preMap[u]:
                if dfs(p,v):
                    return True
            return False
        
        for u, v in queries:
            res.append(dfs(u,v))
            visited = set()
        return res