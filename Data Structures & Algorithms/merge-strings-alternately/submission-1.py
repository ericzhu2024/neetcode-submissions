class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n = min(len(word1), len(word2))
        
        # 1. 交替添加
        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])
        
        # 2. 一次性拼接剩余部分（切片处理）
        res.append(word1[n:])
        res.append(word2[n:])
        
        return "".join(res)