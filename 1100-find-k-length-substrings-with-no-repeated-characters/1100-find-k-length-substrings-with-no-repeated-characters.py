class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        L = len(s)
        if L < k:
            return 0
        elif L == k:
            return 1
        else:
            count = 0
            left, right = 0,k-1
            while(right<L-1):
                if s[left:right] != s[left+1:right+1]:
                    count+=1
                left+=1
                right+=1
        return count//2