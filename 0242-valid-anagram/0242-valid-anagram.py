class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        counter = {}
        for letter in s:
            if letter not in counter:
                counter[letter]=1
            else:
                counter[letter] += 1

        for letter in t:
            if letter not in counter or counter[letter]==0:
                return False
            counter[letter]-=1
        return True
