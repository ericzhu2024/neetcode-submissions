class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in c:
                return [c[num], i]
            c[target-num] = i
        return []