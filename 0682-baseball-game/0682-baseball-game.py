class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = list()
        i = 0
        L = len(operations)
        while(i<L):
            op = operations[i]
            if(op=='+'):
                a = result[-2] + result[-1]
                result.append(a)
            elif(op=='D'):
                a = result[-1] + result[-1]
                result.append(a)
            elif(op=='C'):
                result.pop(-1)
            else:
                result.append(int(op))
            i+=1
        total = 0
        while(len(result)!=0):
            total+=result.pop(-1)
        return total
                
                
        