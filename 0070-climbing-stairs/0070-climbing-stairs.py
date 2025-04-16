class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1,2
        count = 2
        if n==a or n==b:
            return n
        while(count<n):
            a = a + b
            b = a - b
            a = a - b
            b = a + b
            count+=1
        return b