class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        i, L = 0, len(nums)
        while(i<L):
            if nums[i] in hashmap:
                return True
            hashmap.add(nums[i])
            i+=1
        return False  