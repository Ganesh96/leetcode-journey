# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp = [ 0 for _ in range(target+1)]
#         dp[0] = 1
#         for i in range(1,target+1):
#             for num in nums:
#                 if i-num >=0:
#                     dp[i] += dp[i-num]
#         return dp[target]

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(target + 1)]
        dp[0][0] = 1
        
        for i in range(1, target + 1):
            for l in range(1, target + 1):
                for num in nums:
                    if i - num >= 0:
                        dp[i][l] += dp[i - num][l - 1]
        
        return sum(dp[target][1:])
