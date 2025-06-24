import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # Step 1: Count the frequency of each number in the input array.
        # A Counter does this in O(n) time.
        # For nums = [1,1,1,2,2,3], this gives us {1: 3, 2: 2, 3: 1}.
        freq_map = collections.Counter(nums)
        
        # Step 2: Create our "buckets". This is a list of lists.
        # The index of the list represents the frequency.
        # The size is len(nums) + 1 to handle the case where one number appears n times.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Populate the buckets based on frequency.
        # Iterate through the items in our frequency map.
        for num, freq in freq_map.items():
            # Add the number to the bucket corresponding to its frequency.
            buckets[freq].append(num)
            
        # Step 4: Build the result list.
        # Iterate through the buckets from right-to-left (highest frequency to lowest).
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            # For each frequency, add all the numbers from that bucket to the result.
            for num in buckets[i]:
                result.append(num)
            #     # If we have collected k elements, we are done.
                if len(result) == k:
                    return result