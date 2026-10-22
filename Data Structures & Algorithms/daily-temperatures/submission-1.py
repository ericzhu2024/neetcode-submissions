class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                top = stack.pop()
                res[top[0]] = i - top[0]
            stack.append([i,temperatures[i]])
        
        return res
