import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counts = collections.Counter(s)
        t_counts = collections.Counter(t)
        
        # The difference counter will hold excess characters.
        # We only need to count the deficiencies in t, which corresponds
        # to the excess in s.
        diff = s_counts - t_counts
        return sum(diff.values())