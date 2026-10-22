class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = -1 
        while l <= r:
            m = (l + r) // 2
            totalTime = sum([math.ceil(float(p)/m) for p in piles])
            if totalTime > h:
                l = m + 1
            else:
                res = m
                r = m - 1

        return res 