class TwoSum:

    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, number: int) -> None:
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        for nums1 in self.counts:
            nums2 = value - nums1

            if nums2 in self.counts:
                if nums1==nums2:
                    if self.counts[nums1]>=2:
                        return True
                
                else:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)