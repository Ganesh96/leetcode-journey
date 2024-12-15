class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L =  len(nums)
        output = [1] * L
        left = 1
        for i in range(L):
            output[i]*=left
            left*=nums[i]
        
        right = 1
        for i in range(L-1,-1,-1):
            output[i]*=right
            right*=nums[i]
        
        return output