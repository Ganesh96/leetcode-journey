class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half = total_len//2

        if len(A) > len(B):
            A,B = B,A
        
        l,r = 0, len(A)-1
        while True:
            i = (r+l)//2
            j = half-i -2

            aleft = A[i] if i >= 0 else -float('inf')
            aright = A[i+1] if i+1 < len(A) else float('inf')
            bleft = B[j] if j >= 0 else -float('inf')
            bright = B[j+1] if j+1 < len(B) else float('inf')

            if aleft < bright and aright>bleft:
                if total_len%2:
                    return min(bright,aright)
                else:
                    return (max(aleft,bleft) + min(aright,bright))/2
            elif aleft > bright:
                r = i-1
            else:
                l = i+1
        