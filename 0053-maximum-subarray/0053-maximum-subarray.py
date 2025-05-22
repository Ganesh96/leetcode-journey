class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = len(nums)
        curr_sum = max_sum = nums[0]
        for ind in range(1,L):
            curr_sum = max(nums[ind], curr_sum + nums[ind])
            max_sum = max(max_sum, curr_sum)
        return max_sum