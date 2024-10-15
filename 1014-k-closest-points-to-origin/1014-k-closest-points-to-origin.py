import heapq
class Solution:
    def kClosest(self,points, k):
        heap = []
        for x, y in points:
            dist = -(x * x + y * y)  # Use negative distance for max heap
            if len(heap) < k:
                heapq.heappush(heap, (dist, [x, y]))
            else:
                heapq.heappushpop(heap, (dist, [x, y]))
        return [point for (dist, point) in heap]
