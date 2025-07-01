class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # dp[i] will store the length of the LIS ending at index i
        dp = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            # Check all previous elements
            for j in range(i+1,len(nums)):
                # If we can extend the subsequence ending at j...
                if nums[i] < nums[j]:
                    # ...update dp[i] if it creates a longer subsequence
                    dp[i] = max(dp[i], 1 + dp[j])
        
        # The final answer is the maximum value in our dp array
        return max(dp)