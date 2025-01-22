class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx = 0
        odd_idx = 1
        while even_idx < len(nums):
            if nums[even_idx] % 2 != 0:
                while nums[odd_idx] % 2 != 0:
                    odd_idx += 2
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            even_idx += 2
        return nums