class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                res += max(min(leftMax, rightMax) - height[l], 0)
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += max(min(rightMax, leftMax) - height[r], 0)
        
        return res