class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while(start<end):
            mid = (start+end)//2
            print(mid,",",nums[mid])
            if(nums[mid]>=target):
                print("end = mid - 1")
                end = mid
            elif(nums[mid]<target):
                print("start = mid")
                start = mid+1
        return start