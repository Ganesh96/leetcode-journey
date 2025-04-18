class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1 if len(pref)<=len(w) and pref == w[:len(pref)] for w in words else 0 ])