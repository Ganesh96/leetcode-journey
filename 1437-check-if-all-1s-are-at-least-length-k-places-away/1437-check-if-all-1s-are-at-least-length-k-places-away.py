class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        last_one_index = -(k+1)

        for i in range(N):
            if nums[i]==1:
                if i-last_one_index <=k:
                    return False
                last_one_index = i
        return True
