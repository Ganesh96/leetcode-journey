class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = dict()
        res = set()
        for num in arr:
            occ[num] = occ.get(num,0) + 1
        for k,v in occ.items():
            if v not in res:
                res.add(v)
        return len(occ.keys()) == len(res)