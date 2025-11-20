from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # counts = Counter(tasks)
        # maxHeap = [-c for c in counts.values()]

        # heapq.heapify(maxHeap)

        # time = 0
        # q = deque()

        # while maxHeap or q:
        #     time+=1

        #     if maxHeap:
        #         cnt = 1 + heapq.heappop(maxHeap)
        #         if cnt:
        #             q.append([cnt, time+n])
        
        #     if q and q[0][1] == time:
        #         heapq.heappush(maxHeap, q.popleft()[0])
    
        # return time

        counts = Counter(tasks)

        M = max(counts.values())
        C = 0
        for v in counts.values():
            C+= 1 if v==M else 0

        return max((M-1)*(n+1) + C,len(tasks))