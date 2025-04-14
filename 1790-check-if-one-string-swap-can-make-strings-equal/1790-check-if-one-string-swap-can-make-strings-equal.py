class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        log = set()
        c = 2
        index, L = 0, len(s1)
        while(index<L):
            if(s1[index]!=s2[index]):
                log.add(index)
                c-=1
            index+=1
        if c == 2:
            return True
        if c == 0:
            one = log.pop()
            two = log.pop()
            return True if  and s1[one] == s2[two] and s1[two]==s2[one] else False
        return False
                