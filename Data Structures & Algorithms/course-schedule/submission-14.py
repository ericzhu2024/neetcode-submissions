class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for course in graph[cur]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return count == numCourses