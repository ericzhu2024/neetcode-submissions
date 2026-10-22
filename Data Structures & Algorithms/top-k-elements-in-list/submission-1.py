class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)] #create an array with len(nums) + 1 arrays insize of it

        for n in nums:
            count[n] = 1 + count.get(n,0) # if n doesn't exist, return 0

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0 , -1): # from the last item of freq to the first item of freq
                for n in freq[i]:
                    res.append(n)
                    if len(res) == k:
                        return res