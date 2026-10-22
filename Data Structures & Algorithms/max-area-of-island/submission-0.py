class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visited = set()
        res = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r,c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        
        return res