class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0
    def next(self, price: int) -> int:

        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        self.day += 1
        if not self.stack:
            self.stack.append([self.day, price])
            return self.day
        else:
            res = self.day - self.stack[-1][0]
            self.stack.append([self.day, price])
            return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)