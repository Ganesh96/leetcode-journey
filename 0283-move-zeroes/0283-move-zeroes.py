class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hole = 0

        for i, num in enumerate(nums):
            if num!=0 and hole!=i:
                nums[hole] = num
                hole+=1

        for i in range(hole,len(nums)):
            nums[i] = 0
        return nums        