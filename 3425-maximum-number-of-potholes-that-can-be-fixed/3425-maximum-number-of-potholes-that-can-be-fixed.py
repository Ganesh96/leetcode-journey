import heapq

class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        potholes = list()
        series = 0
        for c in road:
            if c == 'x':
                series += 1
            else:
                if series != 0:
                    heapq.heappush(potholes, -series)
                    series = 0

        if series != 0:  # Handle the last series of potholes
            heapq.heappush(potholes, -series)
        print(potholes)

        repaired_potholes = 0
        # while potholes:
        #     block_size = -heapq.heappop(potholes)
        #     repair_cost = block_size + 1
        #     if repair_cost <= budget:
        #         budget -= repair_cost
        #         repaired_potholes += block_size
        #     else:
        #         max_k = min(block_size, budget - 1)
        #         if max_k <= 0:
        #             break
        #         repaired_potholes += max_k
        #         budget -= (max_k + 1) 
        #         break 

        # return repaired_potholes
        result = 0
        while potholes and budget:
            seg =  -heapq.heappop(potholes)
            fix = min(seg, budget - 1)
            result += fix
            budget -= fix + 1
        return result