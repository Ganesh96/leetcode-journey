class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if not (x+y >= target):
            return False
        if target==0:
            return True
        
        def gcd(dx,dy):
            while dy:
                dx,dy =dy, dx%dy
            return dx
        
        return target % gcd(x,y) == 0
        