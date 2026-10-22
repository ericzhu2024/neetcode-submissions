class Solution:
    def groupAnagrams(self, strs: List[str]):
        
        ans = defaultdict(list) 

        for s in strs:
            freq = [0] * 26 

            for i in s:
                freq[ord(i) - ord('a')] += 1
            ans[tuple(freq)].append(s) # list can't be the key of a hashmap in python
        
        return list(ans.values())