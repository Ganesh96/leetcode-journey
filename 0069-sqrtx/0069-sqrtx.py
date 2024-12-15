class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 2
        right = x//2
        while(left<=right):
            root = int((left+right)/2)
            if root*root>x:
                right = root-1
            elif root*root <x:
                left = root + 1
            else:
                return root
        return right
        