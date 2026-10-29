class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        res = ""
        l, r = 0, len(values) - 1
        while l <= r :
            m = l + (r - l) // 2
            t, v = values[m]
            if t > timestamp:
                r = m - 1
            else:
                res = v 
                l = m + 1
        return res
