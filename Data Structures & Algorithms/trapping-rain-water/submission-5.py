class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = [0] * n, [0] * n
        left_max = 0
        right_max = 0
        for i in range(n):
            left_max = max(height[i], left_max)
            l[i] = left_max

        for j in range(n - 1, -1, -1):
            right_max = max(height[j], right_max)
            r[j] = right_max
        res = 0
        for k in range(n):
            res += min(l[k], r[k]) - height[k]
        return res