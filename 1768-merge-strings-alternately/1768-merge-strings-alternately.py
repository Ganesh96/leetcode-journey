class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        l1, l2 = len(word1), len(word2)
        l = l1 if l1>l2 else l2
        for i in range(l):
            if i < l1:
                result += word1[i]
            if i < l2:
                result += word2[i]

        return "".join(result)