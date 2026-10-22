class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self._rob_line(nums[:-1]), self._rob_line(nums[1:]))

    def _rob_line(self, nums: List[int]) -> int:
        rob, skip = 0, 0
        for n in nums:
            rob, skip = skip + n, max(skip, rob)
        return max(rob, skip)