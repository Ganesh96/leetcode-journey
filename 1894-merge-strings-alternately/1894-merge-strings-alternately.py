class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        q = 0
        l = min(len(word1),len(word2))
        res = list()
        while(q<l):
            res.append(word1[q])
            res.append(word2[q])
            q+=1
        res.append(word1[l:])
        res.append(word2[l:])
        return "".join(res)