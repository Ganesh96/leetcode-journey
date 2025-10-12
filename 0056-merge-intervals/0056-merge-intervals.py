class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        output = [intervals[0]]
        for start,end in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start,end])
        return output