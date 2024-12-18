class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        L = len(nums) -1
        new_f = list()
        right = L
        while(left<=right):
            if(abs(nums[left])>abs(nums[right])):
                new_f = [nums[left]] + new_f
                left+=1
            elif(left!=right and abs(nums[left])==abs(nums[right])):
                new_f = [nums[left],nums[right]] + new_f
                left+=1
                right-=1
            else:
                new_f = [nums[right]] + new_f
                right-=1               
        return [f**2 for f in new_f]