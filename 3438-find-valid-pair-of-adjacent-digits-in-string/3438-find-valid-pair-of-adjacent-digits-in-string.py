import collections

class Solution:
    def findValidPair(self, s: str) -> str:
        digit_counts = collections.Counter(s)
        for i in range(len(s) - 1):
            # Get the two adjacent digit characters.
            d1 = s[i]
            d2 = s[i+1]
            
            condition1_met = (d1 != d2)
            condition2_met = (digit_counts[d1] == int(d1))
            condition3_met = (digit_counts[d2] == int(d2))
            
            if condition1_met and condition2_met and condition3_met:
                return d1 + d2
                
        return ""