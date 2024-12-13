class RecentCounter:

    def __init__(self):
        self.recent_requests = list()
        

    def ping(self, t: int) -> int:
        self.recent_requests.append(t)

        anchor = 0
        lower_limit = t-3000

        if lower_limit > 0:
            for time in self.recent_requests:
                if time<lower_limit:
                    anchor+=1
                else:
                    break
            del self.recent_requests[:anchor]

        return len(self.recent_requests)

    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)