class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1),len(str2)

        def isDivisor(l):
            if l1%l or l2%l:
                return False
            f1,f2 = l1//l,l2//l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len(str1),len(str2)),0,-1):
            if(isDivisor(l)):
                return str1[:l]
        return ""