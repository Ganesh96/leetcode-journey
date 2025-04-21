class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False

        l1,l2 = dict(), dict()
        L = len(word1)
        
        for i in range(L):
            l1[word1[i]] = l1.get(word1[i],0) + 1
            l2[word2[i]] = l2.get(word2[i],0) + 1
        ks =[k for k in l1.keys()]

        for k in ks:
            if(l1.get(k,-2)==l2.get(k,-1)):
                del l1[k]
                del l2[k]
        
        if(set(l1.keys())!=set(l2.keys())):
            return False
        u = [i for i in l1.values()]
        v = [i for i in l2.values()]
        return u.sort() == v.sort()