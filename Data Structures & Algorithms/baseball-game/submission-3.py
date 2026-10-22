class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        res = 0

        for o in operations:
            if o == "+":
                res += s[-1] + s[-2]
                s.append(s[-1] + s[-2])
            elif o == "D":
                s.append(2 * s[-1])
                res += 2 * s[-1]
            elif o == "C":
                res -= s.pop()
            else:
                s.append(int(o))
                res += int(o)
        
        return sum(s)