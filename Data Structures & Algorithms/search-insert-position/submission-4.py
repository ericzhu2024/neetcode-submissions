class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            m = l + (r - l)//2
            if nums[m] == target:
                return m 
            elif nums[m] < target:
                res = m + 1
                l = m + 1
            else:
                r = m - 1
        return res