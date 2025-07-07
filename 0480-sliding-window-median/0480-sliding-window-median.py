from typing import List
from heapq import heappop, heappush

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left_heap, right_heap = Solution.build_heaps(nums, k)
        to_remove = dict()
        medians = []

        for i in range(k, len(nums) + 1):
            medians.append(Solution.get_median(left_heap, right_heap, k))

            if i == len(nums):
                break

            balance = 0
            new_element, old_element = nums[i], nums[i-k]

            if old_element not in to_remove:
                to_remove[old_element] = 0
            to_remove[old_element] += 1

            if old_element <= -left_heap[0]:
                balance -= 1
            else:
                balance += 1

            if new_element <= -left_heap[0]:
                heappush(left_heap, -new_element)
                balance += 1
            else:
                heappush(right_heap, new_element)
                balance -= 1

            if balance < 0:
                heappush(left_heap, -heappop(right_heap))
            elif balance > 0:
                heappush(right_heap, -heappop(left_heap))

            while -left_heap[0] in to_remove and to_remove[-left_heap[0]] > 0:
                to_remove[-left_heap[0]] -= 1
                heappop(left_heap)

            while right_heap and right_heap[0] in to_remove and to_remove[right_heap[0]] > 0:
                to_remove[right_heap[0]] -= 1
                heappop(right_heap)


        return medians



    @staticmethod
    def build_heaps(nums, k):
        left_heap, right_heap = [], []

        for i in range(k):
            heappush(left_heap, -nums[i])
            heappush(right_heap, -heappop(left_heap))

            if len(right_heap) > len(left_heap):
                heappush(left_heap, -heappop(right_heap))          

        return left_heap, right_heap

    @staticmethod
    def get_median(left_heap, right_heap, k):
        if k & 1:
            return -left_heap[0]
        else:
            return (-left_heap[0] + right_heap[0])/2