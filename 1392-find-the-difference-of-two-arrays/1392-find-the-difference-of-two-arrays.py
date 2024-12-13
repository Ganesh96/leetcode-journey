class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        f = dict()
        r = [[],[]]
        nums1 = set(nums1)
        nums2 = set(nums2)

        for p in nums1:
            f[p] = 0

        for p in nums2:
            if(p in f.keys()):
                del f[p]
            else:
                f[p] = 1
        
        for k,v in f.items():
            r[v].append(k)
        return r        