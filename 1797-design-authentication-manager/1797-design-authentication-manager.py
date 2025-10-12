class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.registry = dict()
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.registry[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.registry and self.registry[tokenId] > currentTime:
                self.generate(tokenId,currentTime)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        index = 0
        keys = list(self.registry.keys())
        for k in keys:
            if self.registry[k] <= currentTime:
                del self.registry[k]
        return len(self.registry) 


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)