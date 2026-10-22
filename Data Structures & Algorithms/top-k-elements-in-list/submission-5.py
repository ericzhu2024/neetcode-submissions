class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        count = [[] for i in range(len(nums))]

        for n, c in freq.items():
            count[c-1].append(n)

        res = []
        for i in range(len(count)-1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res    