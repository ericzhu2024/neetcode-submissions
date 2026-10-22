class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, output, total):
            if total == target:
                res.append(output.copy())
                return 
            if total > target or i >= len(nums):
                return 
            output.append(nums[i])
            total += nums[i]
            dfs(i, output, total)
            output.pop()
            dfs(i + 1, output, total - nums[i])
        dfs(0, [], 0)
        return res