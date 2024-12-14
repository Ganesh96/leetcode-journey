class MovingAverage:

    def __init__(self, size: int):
        self.data_stream = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        L = len(self.data_stream)
        if L==self.size:
            self.total-=self.data_stream[0]
            self.data_stream.popleft()
            self.data_stream.append(val)
            self.total+=self.data_stream[-1]
        else:
            self.data_stream.append(val)
            self.total+=val
            L+=1
        return self.total if L==1 else self.total/L


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)