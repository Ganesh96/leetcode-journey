class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        zeros = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                zeros +=1
            
            while zeros > k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            w = r-l+1
            max_w = max(max_w,w)
        return max_w