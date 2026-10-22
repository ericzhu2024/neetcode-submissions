class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = 0

        for high in range(len(prices)):
            if prices[high] < prices[low]:
                low = high
            else:
                res = max(res, prices[high] - prices[low])
        return res