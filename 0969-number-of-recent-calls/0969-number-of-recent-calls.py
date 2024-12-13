from collections import deque

class RecentCounter:
    def __init__(self):
        """
        Initializes the counter with zero recent requests.
        """
        self.requests = deque()  # Use a deque to store requests

    def ping(self, t: int) -> int:
        """
        Adds a new request at time t and returns the number of requests 
        that have happened in the past 3000 milliseconds (including the new request).
        """
        self.requests.append(t)  # Add the new request time

        # Remove requests older than 3000 milliseconds
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)  # Return the count of recent requests


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)