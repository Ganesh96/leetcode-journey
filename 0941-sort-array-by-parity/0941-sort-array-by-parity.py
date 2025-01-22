class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        log = {'e':[],'o':[]}
        for i in nums:
            if i%2==0:
                log["e"].append(i)
            else:
                log["o"].append(i)
        res = log["e"] + log["o"]
        return res