class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.registry = {}
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.registry[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.registry and self.registry[tokenId] > currentTime:
            self.registry[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        expired = [k for k, exp in self.registry.items() if exp <= currentTime]
        for k in expired:
            del self.registry[k]
        return len(self.registry)
