class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start, L = 0, len(gain)
        curr = 0
        alt = [0] * (L + 1)
        highest = 0
        while(start< L):
            curr+=gain[start]
            start+=1
            alt[start] = curr
            if highest < curr:
                highest = curr
        return highest
        