from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        pairs =0
        for num in nums:
            hmap[num]+=1
        index = 0
        while(index<len(nums)):
            complement = k - nums[index]
            if hmap[complement] > 0:
                hmap[complement] -=1
                pairs+=1
            index+=1
        return pairs

