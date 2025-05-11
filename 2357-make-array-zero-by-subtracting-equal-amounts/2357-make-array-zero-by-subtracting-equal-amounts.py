class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in set(nums):
            cnt = cnt+1 if i>0 else cnt
        return cnt 
        '''
        3,7,1,5
        2,6,0,4,2
        0,4,0,2,0
        0,2,0,0,0
        0,0,0,0,0


        9,4,6,8,2
        7,2,4,6,0
        5,0,2,4,0
        3,0,0,2,0
        1,0,0,0,0
        0,0,0,0,0
        '''