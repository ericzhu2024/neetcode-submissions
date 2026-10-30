class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            majority = 0
            freq[s[r]] = freq.get(s[r], 0) + 1
            for item, count in freq.items():
                majority = max(majority, count)
            if r - l + 1 - majority > k:
                freq[s[l]] -= 1
                l += 1
                
            res = max(r - l + 1, res)
        return res