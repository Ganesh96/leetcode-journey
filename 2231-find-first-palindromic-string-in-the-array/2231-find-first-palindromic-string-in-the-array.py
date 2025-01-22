class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def check(word)->bool:
            start = 0
            end = len(word)-1
            while(start<end):
                if word[start]!=word[end]:
                    return False
                start+=1
                end-=1
            return True
        
        for word in words:
            if check(word)==True:
                return word
        return ""