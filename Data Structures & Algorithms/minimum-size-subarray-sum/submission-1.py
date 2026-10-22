class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0 
        l = 0 
        csum = 0
        for r in range(len(nums)):
            csum += nums[r]
            if csum >= target and res == 0:
                res = r - l + 1
            while csum - target >= nums[l]:
                csum -= nums[l]
                l += 1
                res = min(r-l+1, res)
        return res