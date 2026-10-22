class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        res = 0
        l = 0
        majority_freq = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            for n, c in window.items():
                majority_freq = max(majority_freq, c)
            
            while r - l + 1 - majority_freq > k:
                window[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res