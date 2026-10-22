class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for n in nums:
            d[n] = d.get(n,0) + 1
        

        for k, v in d.items():
            if v > len(nums) // 2:
                return k