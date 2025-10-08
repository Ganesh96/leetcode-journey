class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hole = 0

        for i, num in enumerate(nums):
            if num!=0:
                if hole!=i:
                    nums[hole] = num
                    nums[i] = 0
                hole+=1
        return nums