class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end =0, len(s) - 1
        s = list(s)
        vowels = set("AaEeIiOoUu")
        while(start<end):
            f1,f2 = True,True
            if s[start] not in vowels:
                start+=1
                f1 = False
            if s[end] not in vowels:
                end-=1
                f2 = False
            if f1 and f2:
                s[start], s[end] = s[end], s[start]
                start+=1
                end-=1
        return "".join(s)