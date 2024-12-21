class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        i, L = 0, len(hamsters)
        res = 0
        while(i<L):
            if hamsters[i]=="H":
                if(i+1<L and hamsters[i+1]=="."):
                    res+=1
                    i+=2
                elif(i-1>=0 and hamsters[i-1]=="."):
                    res+=1
                else:
                    return -1
            i+=1
        return res