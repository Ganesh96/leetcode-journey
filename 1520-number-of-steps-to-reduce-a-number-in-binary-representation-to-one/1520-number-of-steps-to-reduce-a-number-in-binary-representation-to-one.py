class Solution:
    def numSteps(self, s: str) -> int:
        l = [int(i) for i in s]
        steps = 0

        def mov(l):
            index = len(l) - 1
            while index >= 0 and l[index] == 1:
                l[index] = 0
                index -= 1
            if index >= 0: 
                l[index] = 1
            else:
                l.insert(0, 1)

        while len(l) > 1:
            if l[-1] == 0:
                l.pop()
            else:
                mov(l)
            steps += 1

        return steps