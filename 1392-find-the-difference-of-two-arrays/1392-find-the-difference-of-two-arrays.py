class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # f = dict()
        # r = [[],[]]
        # nums1 = set(nums1)
        # nums2 = set(nums2)

        # for p in nums1:
        #     f[p] = 0

        # for p in nums2:
        #     if(p in f.keys()):
        #         del f[p]
        #     else:
        #         f[p] = 1
        
        # for k,v in f.items():
        #     r[v].append(k)
        # return r
        N1 = set(nums1)
        N2 = set(nums2)
        r = [[],[]]
        for n1 in N1-N2:
            r[0].append(n1)
        for n2 in N2-N1:
            r[1].append(n2)
        return r