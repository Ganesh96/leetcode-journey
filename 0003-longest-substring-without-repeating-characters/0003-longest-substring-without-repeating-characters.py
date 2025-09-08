class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = res = 0
        substr = set()
        for right in range(len(s)):
            while(s[right] in substr):
                substr.remove(s[left])
                left+=1
            substr.add(s[right])
            res = max(res, right-left+1)
        return res