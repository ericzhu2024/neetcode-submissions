class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            area = 1
            for dr, dc in directions:
                area += dfs(dr + r, dc + c)
            return area
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                res = max(res, dfs(r, c))
        return res