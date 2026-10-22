class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        count = [[] for x in range(len(nums))]
        for n, c in freq.items():
            count[c-1].append(n)
        
        res = []

        for i in range(len(count)-1 , -1, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
            