class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diff = [0] * len(nums)
        
        for index in range(len(nums)):
            diff[index] = target[index] - nums[index]
        
        total_op = prev_diff = 0
        for current_diff in diff:
            if current_diff * prev_diff < 0:
                total_op+=abs(current_diff)
            
            else:
                total_op+=max(0, abs(current_diff) - abs(prev_diff))
            prev_diff = current_diff
        return total_op
