class Solution:
    def countBits(self, n: int) -> List[int]:
        def cnt(N):
            bits = 0
            while(N>0):
                bits+=N%2
                N//=2
            return bits
        res = list()
        for num in range(n+1):
            res.append(cnt(num))
        return res
            
        