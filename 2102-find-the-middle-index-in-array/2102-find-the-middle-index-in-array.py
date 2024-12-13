class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        anchor = 0
        L = len(nums)
        total = l_sum = 0
        for index in range(1,L):
            total+=nums[index]
        
        while(anchor<L-1 and l_sum!=total):
            l_sum+=nums[anchor]
            anchor+=1
            total-=nums[anchor]
        return -1 if l_sum!=total  else anchor
        