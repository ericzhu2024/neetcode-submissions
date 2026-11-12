class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for crs, pre in prerequisites:
            indegree[crs] += 1
            graph[pre].append(crs)
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        output = []
        while q:
            cur = q.popleft()
            output.append(cur)
            for crs in graph[cur]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        if len(output) != numCourses:
            return []
        return output