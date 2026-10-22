class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            middle = (l + r)//2
            row = middle // COLS
            col = middle % COLS

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = middle + 1
            else:
                r = middle - 1
        return False