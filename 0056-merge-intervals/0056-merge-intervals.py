class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]
        
        for s,e in intervals:
            if s <= output[-1][1]:
                output[-1][1] = max(e,output[-1][1])
            
            else:
                output.append([s,e])
        return output



