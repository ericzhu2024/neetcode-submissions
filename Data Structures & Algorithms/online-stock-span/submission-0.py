class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        temp = []
        res = 0
        while self.stack and self.stack[-1] <= price:
            temp.append(self.stack.pop())
            res += 1
        for i in range(len(temp)-1,-1,-1):
            self.stack.append(temp[i])
        self.stack.append(price)
        return res  + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)