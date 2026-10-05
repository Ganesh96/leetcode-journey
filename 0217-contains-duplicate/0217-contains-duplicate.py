class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicates = set()
        for item in nums:
            if item in duplicates:
                return True
            duplicates.add(item)
        return False
        