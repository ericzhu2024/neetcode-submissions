class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visit = set()
        def dfs(i, par):
            if i in visit:
                return False
            
            visit.add(i)
            for n in graph[i]:
                if n == par:
                    continue
                if not dfs(n, i):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n