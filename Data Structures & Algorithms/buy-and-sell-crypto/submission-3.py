class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for n in prices:
            if n < buy:
                buy = n
            res = max(res, n - buy)
        return res