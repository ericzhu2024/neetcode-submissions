class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        e_c = {}

        for n in nums:
            e_c[n] = e_c.get(n, 0) + 1
        
        c_e = [[] for i in range(len(nums))]

        for e, c in e_c.items():
            c_e[c-1].append(e)
        
        res = []

        for i in range(len(nums) - 1, -1, -1):
            for element in c_e[i]:
                res.append(element)
                if len(res) == k:
                    return res

        