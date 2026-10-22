class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            alive = True

            while alive and n < 0 and stack and stack[-1] > 0:
                if n + stack[-1] < 0:
                    stack.pop()
                    continue
                elif n + stack[-1] == 0:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            
            if alive:
                stack.append(n)
        return stack
                    
