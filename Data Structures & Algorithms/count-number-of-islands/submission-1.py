class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                return False
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return True
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    res += 1
        return res
