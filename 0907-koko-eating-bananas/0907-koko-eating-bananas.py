from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while(start<end):
            mid = ( start + end ) // 2
            if(self.validate_h(mid,h,piles)):
                end = mid
            else:
                start = mid + 1
        return start

    def validate_h(self,k,h,piles)->bool:
        temp_h = 0
        for pile in piles:
            temp_h+= ceil(pile/k)
        return temp_h<=h