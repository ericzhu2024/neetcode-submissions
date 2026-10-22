class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0

        cur_sum = 0

        prefix_sums = {0: 1}


        for num in nums:
            cur_sum += num

            if cur_sum - k in prefix_sums:
                count += prefix_sums[cur_sum - k]

            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
        return count