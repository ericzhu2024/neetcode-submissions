class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], [False] * len(nums), nums)
        return self.res

    def backtrack(self, perm, pick, nums):
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return 
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm,pick,nums)
                perm.pop()
                pick[i] = False
        