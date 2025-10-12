class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start,end):
            while(start<end):
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
        L = len(nums)-1
        k = k% L
        reverse(0,L)
        reverse(0,k-1)
        reverse(k,L)