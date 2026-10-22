class Solution:
    def isValid(self, s: str) -> bool:
        p = { ')':'(', '}':'{', "]": "["}

        stack = []

        for c in s:
            if c not in p:
                stack.append(c)
            else:
                if stack and p[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            