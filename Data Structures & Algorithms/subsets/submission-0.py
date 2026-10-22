class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for i in range(len(nums)):
            l = len(res)
            for j in range(l):
                res.append(res[j] + [nums[i]])
        return res
