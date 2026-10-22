class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. build element -> frequency map O(n)
        #2. build frequency -> elements map O(n)
        #3. append top k frequent element to res array O(k)

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        count = [[] for _ in range(len(nums))]

        for e, c in freq.items():
            count[c - 1].append(e)
        
        res = []
        for i in range(len(count) - 1, -1, -1):
            arr = count[i]
            for n in arr:
                res.append(n)
                if len(res) == k:
                    return res