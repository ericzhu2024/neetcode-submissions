class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
                if element in rows[r] or element in cols[c] or element in grids[r//3][c//3]:
                    return False
                rows[r].add(element)
                cols[c].add(element)
                grids[r//3][c//3].add(element)
        return True