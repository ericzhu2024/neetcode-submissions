class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        distance = 0
        while q:
            distance += 1
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row < 0 or col < 0 or row >= rows or col >= cols:
                        continue
                    if grid[row][col] == 2147483647:
                        grid[row][col] = distance
                        q.append((row, col))
        