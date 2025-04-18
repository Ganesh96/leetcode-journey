class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def check_prefix(word)->int:
            for index in range(len(pref)):
                if pref[index] != word[index]:
                    return 0
            return 1
        count = 0
        for w in words:
            if len(pref)<=len(w):
                count+=check_prefix(w)
        return count