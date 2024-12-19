class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        logs = {}
        l = len(nums)
        for ind in range(l):
            need = target - nums[ind]
            if(need not in logs.keys()):
                logs[nums[ind]] = ind
            else:
                return [ind,logs[need]]
        