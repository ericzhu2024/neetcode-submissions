class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return []
        freq = {}

        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        count = [[] for _ in range(len(nums))]
        for n, f in freq.items():
            count[f - 1].append(n)

        res = []
        for i in range(len(count) - 1, -1, -1):
            for val in count[i]:
                res.append(val)
                if len(res) == k:
                    return res