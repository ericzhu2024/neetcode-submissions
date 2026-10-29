class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if not values or timestamp < values[0][0]:
            return ""
        l, r = 0, len(values) - 1
        while l <= r :
            m = l + (r - l) // 2
            t, v = values[m]
            # if t == timestamp:
            #     return v
            # elif t > timestamp:
            #     r = m - 1
            # else:
            #     l = m + 1
            if t > timestamp:
                r = m - 1
            else:
                l = m + 1
        return values[r][1] 
