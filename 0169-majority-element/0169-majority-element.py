class Solution:
    def majorityElement(self, nums):
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
        nums.sort()
        l = len(nums)
        return nums[l//2]