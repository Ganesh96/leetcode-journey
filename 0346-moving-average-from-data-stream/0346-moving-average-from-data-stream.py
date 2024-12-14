class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.data = deque()
    def next(self, val: int) -> float:
        self.data.append(val)
        L = len(self.data)#4
        summed = 0
        while self.data and L > self.size:
              self.data.popleft()
              L-=1
        summed = sum(self.data)
        return summed/L
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)