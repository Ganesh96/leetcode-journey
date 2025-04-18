class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        return words == ["".join(x) for x in zip_longest(*words, fillvalue="")]