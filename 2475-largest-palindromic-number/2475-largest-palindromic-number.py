from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        if len(num.replace('0', '')) == 0:
            return "0"

        counts = Counter(num)
        maxOdd = '-1'
        ans = []

        for key in sorted(counts.keys(), reverse=True):
            if counts[key] // 2 > 0:
                if ans or (not ans and key != '0'):
                    ans.extend([key] * (counts[key] // 2))

            if counts[key] % 2 == 1:
                maxOdd = max(key, maxOdd)

        strAns = "".join(ans)
        return strAns + maxOdd + strAns[::-1] if maxOdd > '-1' else strAns + strAns[::-1]


        