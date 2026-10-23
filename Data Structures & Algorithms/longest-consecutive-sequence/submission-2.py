class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in numset:
                steak = 1
                while n + steak in numset:
                    steak += 1
                res = max(steak, res)
        return res