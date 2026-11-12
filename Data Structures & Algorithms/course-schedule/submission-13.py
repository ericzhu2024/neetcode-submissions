class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        visited = set()

        def dfs(i):
            if i in visited:
                return False
            if graph[i] == []:
                return True
            visited.add(i)

            for n in graph[i]:
                if not dfs(n):
                    return False
            visited.remove(i)
            graph[i] = []
            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True