class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f = dict()
        t = set()
        for i in arr:
            f[i] = f.get(i,0) + 1
        for k,v in f.items():
            if v in t:
                return False
            t.add(v)
        return True