class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                a, b = stack.pop(), stack.pop()
                c = b // a
                if c < 0:
                    stack.append(-(abs(b)//abs(a)))
                else:
                    stack.append(c)
            else:
                stack.append(int(t))
        return stack[-1]