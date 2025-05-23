class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        
        differences = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differences.append(i)
                if len(differences) > 2:
                    return False
        
        if len(differences) != 2:
            return False
        
        i, j = differences
        return s1[i] == s2[j] and s1[j] == s2[i]