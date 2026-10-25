class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [(position[i], speed[i]) for i in range(len(speed))]
        stack.sort()
        res = 0
        while stack:
            pos, speed = stack.pop()
            time = (target - pos) / speed
            while stack:
                next_pos, next_speed = stack[-1]
                if (target - next_pos) / next_speed <= time:
                    stack.pop()
                else:
                    break
            res += 1
        return res

