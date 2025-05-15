class Logger:

    def __init__(self):
        self.remind = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.remind.keys() and timestamp<self.remind[message]:
            return False
        else:
            self.remind[message] = 10 + timestamp
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)