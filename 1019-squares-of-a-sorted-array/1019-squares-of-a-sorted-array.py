class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] * nums[left])
                left += 1
            else:
                result.append(nums[right] * nums[right])
                right -= 1
        return result[::-1]