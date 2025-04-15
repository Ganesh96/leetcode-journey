class Solution:
    def confusingNumber(self, n: int) -> bool:
        old_n = n
        rotate = {0:0,1:1,6:9,8:8,9:6}
        stack = list()
        res = 0
        while(n>0):
            q = n%10
            n = n//10
            if q not in rotate.keys():
                return False
            #old_n = old_n*10+q
            stack.append(q)

        for q in range(0,len(stack)):
            res = res*10 + rotate.get(stack[q],0)
        return old_n!=res