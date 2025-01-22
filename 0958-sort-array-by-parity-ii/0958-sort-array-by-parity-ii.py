class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_nums = []
        odd_nums = []
        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)

        result = [0] * len(nums)
        even_idx = 0
        odd_idx = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result[i] = even_nums[even_idx]
                even_idx += 1
            else:
                result[i] = odd_nums[odd_idx]
                odd_idx += 1
        return result