class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            preMap[c].append(p)
        output = []
        visited, cycle = set(), set()

        def dfs(i):
            if i in cycle:
                return False 
            if i in visited:
                return True 
            cycle.add(i)
            for p in preMap[i]:
                if not dfs(p):
                    return False
            cycle.remove(i)
            visited.add(i)
            output.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
