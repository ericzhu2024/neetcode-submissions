class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        l, r = 0, ROW * COL - 1
        while l <= r:
            m = l + (r - l) // 2
            row = m // COL
            col = m % COL
            cur = matrix[row][col]
            if cur == target:
                return True
            elif cur > target:
                r = m - 1
            else:
                l = m + 1
        return False