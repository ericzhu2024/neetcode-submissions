class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r - l)//2
            time = sum([math.ceil(i/k) for i in piles])
            if time > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res
