class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_index = 0
        curr_index = 0
        l = len(nums)
        while(curr_index<l):
            if nums[curr_index]==val:
                curr_index+=1
                continue
            nums[new_index]= nums[curr_index]
            new_index+=1
            curr_index+=1
        return new_index
        