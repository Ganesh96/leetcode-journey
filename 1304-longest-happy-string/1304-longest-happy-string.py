import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []
        for count, ch in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:  # Only add characters with non-zero counts to the heap
                heapq.heappush(maxHeap, (count, ch))

        while maxHeap:
            count1, char1 = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-2] == res[-1] == char1:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char1
                count1 += 1
            if count1:
                heapq.heappush(maxHeap, (count1, char1))
        return res