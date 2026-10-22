class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = l
        while l <= r:
            m = (l + r)//2
            if nums[r] > nums[m]:
                r = m
            else:
                res = l
                l = m + 1
        return nums[res]