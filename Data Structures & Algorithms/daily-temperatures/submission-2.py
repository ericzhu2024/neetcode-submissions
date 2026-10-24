class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            cur = temperatures[i]
            while stack and stack[-1][0] < cur:
                _, index = stack.pop()
                res[index] = i - index

            stack.append([cur, i])
        return res

        
