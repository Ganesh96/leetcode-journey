class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # base case: empty string is breakable

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in word_set:
                    dp[i] = True
                    break
                # if dp[j] is True and s[j:i] in word_set:
                    # dp[i] = True
                    # break

        return dp[n]
