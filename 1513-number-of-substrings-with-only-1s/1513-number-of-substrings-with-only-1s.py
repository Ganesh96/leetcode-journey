class Solution:
    def numSub(self, s: str) -> int:
        total_count = current_length = 0
        MOD = 10^9 + 7
        i = 0
        N = len(s)
        while(i<N):
            current_length = current_length + 1 if s[i]=='1' else 0
            total_count = (total_count + current_length) % MOD
            i+=1
        return total_count
            
