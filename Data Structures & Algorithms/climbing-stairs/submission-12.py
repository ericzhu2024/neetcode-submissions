class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = {1: 1, 2: 2}
        def helper(n):
            if n in self.dp:
                return self.dp[n]
            self.dp[n] = helper(n - 1) + helper(n - 2)
            return self.dp[n]
        
        return helper(n)