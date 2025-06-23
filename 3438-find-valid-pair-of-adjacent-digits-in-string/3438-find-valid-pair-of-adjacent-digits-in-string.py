class Solution:
    def findValidPair(self, s: str) -> str:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in range(len(s) - 1):
            first = s[i]
            second = s[i + 1]
            if first != second and freq[first] == int(first) and freq[second] == int(second):
                return first + second
        return ""
        