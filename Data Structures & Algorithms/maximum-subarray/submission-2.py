class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        res = float("-inf")
        for n in nums:
            cur_sum += n
            res = max(res, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return res