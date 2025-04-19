import heapq
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        L = len(reward1)
        t = 0 
        d = []
        index = 0
        for i in range(len(reward2)):
            t+=reward2[i]
            d.append(reward1[i]-reward2[i])
        sorting = heapq.nlargest(k,d)
        return t + sum(sorting) 
    