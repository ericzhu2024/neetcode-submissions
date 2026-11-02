class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # visit = set()
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]


        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return 
            # visit.add((r, c))
            board[r][c] = 'T'
            for dr, dc in directions:
                dfs(dr + r, dc + c)
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    if board[r][c] == 'O':
                        dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'