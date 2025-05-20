class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        count,running_and = 0, ~0
        for num in nums:
            running_and &= num
            if running_and==0:
                count += 1
                running_and = ~0
        return max(1,count)