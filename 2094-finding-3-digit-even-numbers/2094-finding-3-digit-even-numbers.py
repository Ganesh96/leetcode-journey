from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = set()
        
        for d1 in range(1, 10):
            if freq[d1] == 0:
                continue
            freq[d1] -= 1
            for d2 in range(0, 10):
                if freq[d2] == 0:
                    continue
                freq[d2] -= 1
                for d3 in [0, 2, 4, 6, 8]:
                    if freq[d3] == 0:
                        continue
                    num = 100*d1 + 10*d2 + d3
                    res.add(num)
                freq[d2] += 1
            freq[d1] += 1
        
        return sorted(res)
