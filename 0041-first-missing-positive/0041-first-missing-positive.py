class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        L = len(nums)
        for i in range(L):
            if nums[i]<0:
                nums[i] = 0
        
        for i in range(L):
            val = abs(nums[i])
            if 1 <= val <= L:
                if nums[val-1]>0:
                    nums[val-1]*=-1
                elif nums[val-1]==0:
                    nums[val-1] = -(L+1)
        

        for i in range(1,L+1):
            if nums[i-1]>=0:
                return i
        return L+1

        