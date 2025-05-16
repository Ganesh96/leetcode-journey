class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        near = -1
        for index, dxy in enumerate(points):
            dx, dy = dxy
            if dx==x or dy==y:
                dist  = abs(x-dx) + abs(y-dy)
                if min_dist> dist:
                    min_dist = dist
                    near = index
        return near
        