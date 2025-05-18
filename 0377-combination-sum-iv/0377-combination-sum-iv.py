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
    def combinationSum4(self, nums: List[int], target: int, max_len: int = 100) -> int:
        OFFSET = 10 * max_len
        dp = [[0] * (max_len + 1) for _ in range(2 * OFFSET + 1)]
        dp[OFFSET][0] = 1  # sum=0, length=0
        
        for l in range(1, max_len + 1):
            for s in range(-OFFSET, OFFSET + 1):
                for num in nums:
                    prev = s - num
                    if -OFFSET <= prev <= OFFSET:
                        dp[s + OFFSET][l] += dp[prev + OFFSET][l - 1]
        
        total = 0
        for l in range(1, max_len + 1):
            total += dp[target + OFFSET][l]
        return total

