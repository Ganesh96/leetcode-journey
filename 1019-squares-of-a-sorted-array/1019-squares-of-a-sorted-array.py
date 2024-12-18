class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        L = len(nums) -1
        new_f = list()
        right = L
        while(left<=right):
            if(abs(nums[left])>abs(nums[right])):
                new_f = [nums[left]**2] + new_f
                left+=1
            elif(left!=right and abs(nums[left])==abs(nums[right])):
                new_f = [nums[left]**2]*2 + new_f
                left+=1
                right-=1
            else:
                new_f = [nums[right]**2] + new_f
                right-=1               
        return new_f