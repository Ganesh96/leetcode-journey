class Solution:
    def countBits(self, n: int) -> List[int]:
        res = list()
        for num in range(n+1):
            res.append(num.bit_count())
        return res