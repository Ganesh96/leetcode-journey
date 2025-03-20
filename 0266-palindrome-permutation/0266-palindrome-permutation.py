class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = dict()
        for letter in s:
            count[letter] = count.get(letter,0) + 1
        odd = 0
        for _,v in count.items():
            if v%2==1:
                odd+=1
        return True if odd<=1 else False