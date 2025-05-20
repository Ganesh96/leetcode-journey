class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        L = len(arr)
        dp = [0] * (L + 1)

        for i in range(1, L + 1):
            max_val = 0
            for j in range(1, min(k, i) + 1):
                max_val = max(max_val, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + max_val * j)

        return dp[L]
