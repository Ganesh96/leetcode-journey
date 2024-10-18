from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialize frequency counts for s1 and the first window in s2 using Counter (hashmap)
        s1Count = Counter(s1)
        s2Count = Counter(s2[:len(s1)])

        # Slide the window over s2
        for i in range(len(s2) - len(s1)):
            # If the frequency counts match, return True
            if s1Count == s2Count:
                return True

            # Remove the character going out of the window (s2[i])
            s2Count[s2[i]] -= 1
            if s2Count[s2[i]] == 0:
                del s2Count[s2[i]]  # Remove the key from the hashmap if the count becomes zero

            # Add the new character coming into the window (s2[i + len(s1)])
            s2Count[s2[i + len(s1)]] += 1

        # Check the last window
        return s1Count == s2Count
