class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if r >= ROW or c >= COL or r < 0 or c < 0 or (r,c) in visited or grid[r][c] == '0':
                return False
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return True
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c):
                    res += 1
        return res 