class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for n in asteroids:
            broken = False
            while stack and n < 0 < stack[-1]:
                top = stack[-1]
                if  top > -n:
                    broken = True
                    break
                elif top == -n:
                    broken = True
                    stack.pop()
                    break
                else:
                    stack.pop()
            if broken == False:
                stack.append(n)
        return stack