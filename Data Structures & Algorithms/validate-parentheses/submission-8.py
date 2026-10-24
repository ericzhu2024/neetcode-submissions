class Solution:
    def isValid(self, s: str) -> bool:
        c_o = {']':'[', '}':'{', ')':'('}

        stack = []

        for c in s:
            if c in c_o:
                if not (stack and c_o[c] == stack.pop()):
                    return False
            else:
                stack.append(c)
        return not stack