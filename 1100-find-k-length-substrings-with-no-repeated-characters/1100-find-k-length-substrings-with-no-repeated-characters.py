class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        seen = set()
        count = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            if right - left + 1 == k:
                count += 1
                seen.remove(s[left])
                left += 1
        return count