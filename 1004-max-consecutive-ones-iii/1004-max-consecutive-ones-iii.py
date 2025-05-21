# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
        # left = 0
        # max_len = 0
        # zeros = 0

        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         zeros += 1
        #     while zeros > k:
        #         if nums[left] == 0:
        #             zeros -= 1
        #         left += 1
        #     max_len = max(max_len, right - left + 1)

        # return max(max_len, right - left + 1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,mx = 0,0
        for r,n in enumerate(nums):
            k-=(1-n)
            if k<0:
                k+=(1-nums[l])
                l+=1
            mx = max(mx,r-l+1)
        return mx
    