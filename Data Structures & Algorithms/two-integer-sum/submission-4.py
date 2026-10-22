class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} # key = elements in nums; value = index in nums

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap: # to check if numMap has the key
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return [] 