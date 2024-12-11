class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        q1, q2 = 0,0
        l1,l2 = len(word1),len(word2)
        res = ""
        while(q1<l1 and q2<l2):
            res+=word1[q1]
            res+=word2[q2]
            q1+=1
            q2+=1
        if(q1<l1):
            res+=word1[q1:]
        elif(q2<l2):
            res+=word2[q2:]
        return res
        
        