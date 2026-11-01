class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROW, COL = len(grid), len(grid[0])
        
        q = deque()
        def addCell(r, c):
            if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in visited or grid[r][c] == -1:
                return 
            visited.add((r, c))
            q.append([r, c])


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    addCell(dr + r, dc + c)
            dist += 1
        