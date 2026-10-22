class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        res = r


        def canShip(cap):
            count, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    count += 1
                    if count > days:
                        return False
                    currCap = cap
                currCap -= w
            return True

        while l <= r:
            m = l + (r - l) // 2
            if canShip(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res