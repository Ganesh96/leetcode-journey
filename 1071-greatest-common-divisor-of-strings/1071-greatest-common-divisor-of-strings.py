class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        L = len(str1) if len(str1)< len(str2) else len(str2)
        
        def div(l):
            if len(str1)%l!=0 or len(str2)%l!=0:
                return False
            m1, m2 = len(str1)//l,len(str2)//l
            return m1*str1[:l] == str1 and m2*str1[:l] == str2
        res = 0
        for l in range(L,0,-1):
            if div(l):
                return str1[:l]
        return ""