class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = ''
        for i in range(n):
            res += word1[i]
            res += word2[i]
        res += word1[n::]
        res += word2[n::]
        return res