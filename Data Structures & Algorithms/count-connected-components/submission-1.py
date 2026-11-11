class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            neighbors = graph[i]
            for n in neighbors:
                dfs(n)
            return True
        
        res = 0
        for node in range(n):
            if dfs(node):
                res += 1
        return res