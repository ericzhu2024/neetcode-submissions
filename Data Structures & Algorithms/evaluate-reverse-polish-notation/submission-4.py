class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                a,b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif t == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                a,b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == "/":
                a,b = stack.pop(), stack.pop()
                c = int(b/a)
                stack.append(c)
            else:
                stack.append(int(t))
        return stack[0]