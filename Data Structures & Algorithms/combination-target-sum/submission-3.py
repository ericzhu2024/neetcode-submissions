class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, path = [], []

        def dfs(start):
            if sum(path) == target:
                res.append(path[:])
            if sum(path) > target:
                return 
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i)
                path.pop()
        
        dfs(0)
        return res
