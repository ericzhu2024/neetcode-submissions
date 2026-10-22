class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l = min(len(word1), len(word2))
        for i in range(l):
            res.append(word1[i])
            res.append(word2[i])
        if len(word1) > len(word2):
            res.append(word1[i + 1:])
        else:
            res.append(word2[i + 1:])
        return "".join(res)