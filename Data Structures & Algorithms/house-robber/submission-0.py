class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, skip = 0, 0
        for n in nums:
            rob, skip = skip + n, max(rob, skip)
        return max(rob, skip)