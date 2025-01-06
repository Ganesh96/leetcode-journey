class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        L = len(nums)
        res = [-1] * (2*L)
        for index in range(L):
            res[index] = nums[index]
            res[index+L] = nums[index]
        return res
        