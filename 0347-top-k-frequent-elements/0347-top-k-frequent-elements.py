class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        freq = [[] for _ in range(len(nums)+ 1)]
        res = list()
        for n in nums:
            count[n] = count.get(n,0) + 1
        
        for n,c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                if k == 0:
                    return res
                res.append(n)
                k-=1
        return nums