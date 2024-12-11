class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great = max(candies)
        return [i + extraCandies >= great for i in candies]