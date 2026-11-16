class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        def dfs(start):
            res.append(path[:])             # 每个节点都记录
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1)                  # 只往后选，避免 [1,2] 和 [2,1] 重复
                path.pop()
        dfs(0)
        return res