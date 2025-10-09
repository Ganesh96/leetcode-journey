class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for num in nums:
            currSum = num if currSum < 0 else currSum+num
            maxSum = max(maxSum, currSum)
        return maxSum