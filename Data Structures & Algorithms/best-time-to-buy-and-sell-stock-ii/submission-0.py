class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0, 1
        highest = prices[0]
        profit = 0
        while l < len(prices) and r < len(prices):
            if prices[r] < highest:
                profit += highest - prices[l]
                l = r 
            
            highest = prices[r]
            r += 1
        if (prices[r - 1] - prices[l]) > 0:
            profit += prices[r - 1] - prices[l]
        return profit


                                
