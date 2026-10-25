class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        cur_time = 0.0
        for pos, spd in cars:
            t = (target - pos) / spd
            if t > cur_time:      # 追不上前面的车队 → 新车队
                fleets += 1
                cur_time = t
        return fleets

