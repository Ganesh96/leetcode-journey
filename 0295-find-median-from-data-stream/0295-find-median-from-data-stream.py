import heapq

class MedianFinder:
    def __init__(self):
        """
        Initializes the data structure with two heaps.
        `small_half`: A max-heap to store the smaller half of the numbers.
        `large_half`: A min-heap to store the larger half of the numbers.
        """
        # We store negative numbers in small_half to simulate a max-heap with heapq.
        self.small_half = []
        self.large_half = []

    def addNum(self, num: int) -> None:
        # This is a balanced and robust way to add a number.

        # Step 1: Always add the new number to the max-heap (small_half).
        heapq.heappush(self.small_half, -1 * num)
        
        # Step 2: To maintain the heap property (all smalls <= all larges),
        # move the largest element from the small_half to the large_half.
        largest_in_small_half = -1 * heapq.heappop(self.small_half)
        heapq.heappush(self.large_half, largest_in_small_half)
        
        # Step 3: Now, balance the sizes. If the large_half has grown too big,
        # move its smallest element back to the small_half.
        # We want small_half to be equal to or one larger than large_half.
        if len(self.large_half) > len(self.small_half):
            smallest_in_large_half = heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -1 * smallest_in_large_half)

    def findMedian(self) -> float:
        # Step 1: Check if the total number of elements is odd or even
        # by comparing the heap sizes.
        
        # If the sizes are equal, the total count is even.
        if len(self.small_half) == len(self.large_half):
            # The median is the average of the two middle elements
            # (the tops of our heaps).
            # Remember to negate the value from the max-heap.
            return (-self.small_half[0] + self.large_half[0]) / 2.0
            
        else: # The total count is odd.
            # By our addNum logic, the small_half will always have the extra element.
            # The median is the single middle element.
            return float(-self.small_half[0])