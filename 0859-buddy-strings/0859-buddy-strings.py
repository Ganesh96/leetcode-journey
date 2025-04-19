class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if goal==s:
            return len(set(s)) < len(s)
        curr, end = 0, len(s)
        one,two = -1,-1
        diff = 2
        while(curr<end):
            if s[curr] != goal[curr]:
                diff-=1
                if one == -1:
                    one = curr
                elif two ==-1:
                    two = curr
            if diff<0:
                return False
            curr+=1
        print(diff,one,two)
        if s[one] == goal[two] and s[two] == goal[one] and diff==0:
            return True
        else:
            return False