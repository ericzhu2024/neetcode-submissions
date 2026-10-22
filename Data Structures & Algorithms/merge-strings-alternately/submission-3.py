class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l = min(len(word1), len(word2))
        for i in range(l):
            res.append(word1[i])
            res.append(word2[i])

        res.append(word1[l:])
        res.append(word2[l:])

        return "".join(res)