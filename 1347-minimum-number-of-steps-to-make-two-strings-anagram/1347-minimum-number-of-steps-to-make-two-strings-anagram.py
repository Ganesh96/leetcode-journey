import collections

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Step 1: Create a frequency map of all characters needed for string `s`.
        s_counts = collections.Counter(s)

        # `steps` will count the number of characters in `s` that are
        # not accounted for by the characters in `t`.
        steps = 0
        
        # Step 2: Iterate through the characters of string `t`.
        for char in t:
            # If `t` has a character that is also needed by `s`...
            if s_counts[char] > 0:
                # ...then this character is "correct" and we use one up.
                s_counts[char] -= 1
        
        # Step 3: The remaining counts in `s_counts` represent the characters
        # that `s` needed but `t` did not provide. The sum of these counts
        # is the number of characters that must be changed in `t`.
        for count in s_counts.values():
            steps += count
            
        return steps

# # A more concise version of the same logic:
# class SolutionConcise:
#     def minSteps(self, s: str, t: str) -> int:
#         s_counts = collections.Counter(s)
#         t_counts = collections.Counter(t)
        
#         # The difference counter will hold excess characters.
#         # We only need to count the deficiencies in t, which corresponds
#         # to the excess in s.
#         diff = s_counts - t_counts
#         return sum(diff.values())