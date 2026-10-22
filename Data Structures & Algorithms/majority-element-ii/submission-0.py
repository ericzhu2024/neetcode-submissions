class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        count = {}

        for n in nums:
            count[n]  = count.get(n, 0) + 1

        for k, v in count.items():
            if v > len(nums) // 3:
                res.append(k)
        return res