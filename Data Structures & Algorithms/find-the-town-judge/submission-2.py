class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        credit = defaultdict(int)

        for src, dst in trust:
            credit[src] = credit.get(src, 0) - 1
            credit[dst] = credit.get(dst, 0) + 1
        
        for i in range(1, n + 1):
            if credit[i] == n - 1:
                return i
        
        return -1