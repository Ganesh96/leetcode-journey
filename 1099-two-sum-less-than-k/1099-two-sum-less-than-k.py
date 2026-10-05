class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        max_sum = -1
        nums.sort()
        left, right = 0, len(nums) - 1
        while(left< right):
            cur_sum = nums[left] + nums[right]
            if cur_sum < k:
                max_sum = max(max_sum,cur_sum)
                left+=1
            if cur_sum >= k:
                right-=1
        return max_sum