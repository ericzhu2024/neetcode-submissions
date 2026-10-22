class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0] * len(height)
        rmax = [0] * len(height)

        lm = 0
        for i in range(len(height)):
            lmax[i] = lm
            if height[i] > lm:
                lm = height[i]
        
        rm = 0
        for j in range(len(height) - 1, -1, -1):
            rmax[j] = rm
            if height[j] > rm:
                rm = height[j]
        
        res = 0
        for k in range(len(height)):
            if min(lmax[k],rmax[k]) > height[k]:
                res += min(lmax[k], rmax[k]) - height[k]
        return res