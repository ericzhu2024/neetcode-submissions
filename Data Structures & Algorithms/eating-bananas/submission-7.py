class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        def canFinish(m):
            return sum([math.ceil(x/m) for x in piles]) <= h
        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2
            if canFinish(m):
                r = m - 1
            else:
                l = m + 1
        return l