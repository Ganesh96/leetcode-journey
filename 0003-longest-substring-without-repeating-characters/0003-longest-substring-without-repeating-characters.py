class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        l = max_length = 0

        for r in range(len(s)):
            while(s[r] in visit):
                visit.remove(s[l])
                l+=1
            visit.add(s[r])
            max_length = max(r-l+1, max_length)
        return max_length