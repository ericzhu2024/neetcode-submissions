class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        time = 0
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row < 0 or col < 0 or row >= rows or col >= cols:
                        continue
                    if grid[dr + r][dc + c] == 1:
                        grid[dr + r][dc + c] = 2
                        fresh -= 1
                        q.append((dr + r, dc + c))
            time += 1
        
        if fresh != 0:
            return -1
        else:
            return time
