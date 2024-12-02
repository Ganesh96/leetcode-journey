class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I':1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        ans,ind = 0,0
        l = len(s)
        while(ind<l):
            if(ind+1 < l  and nums[s[ind]]<nums[s[ind+1]]):
                print(s[ind]," > ",s[ind+1])
                ans+= nums[s[ind+1]]-nums[s[ind]] # CM = m-c = 1000-100
                print(">>>",ans)
                ind+=2
            else:
                ans+=nums[s[ind]]
                ind+=1
        return ans
