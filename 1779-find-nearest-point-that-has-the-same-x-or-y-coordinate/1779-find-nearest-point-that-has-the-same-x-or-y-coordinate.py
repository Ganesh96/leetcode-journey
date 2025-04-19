class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        near = -1
        for rank,dxy in enumerate(points):
            dx, dy = dxy
            if dx==x or dy==y:
                dist  = abs(dx-x) + abs(dy-y)
                if min_dist> dist:
                    min_dist = dist
                    near = rank
        return near
        