class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self._rob_line(nums[:-1]), self._rob_line(nums[1:]))

    def _rob_line(self, nums: List[int]) -> int:
        prev, cur = 0, 0   # prev = dp[i-2], cur = dp[i-1]
        for x in nums:
            prev, cur = cur, max(cur, prev + x)
        return cur