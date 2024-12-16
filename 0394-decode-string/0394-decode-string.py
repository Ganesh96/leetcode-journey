class Solution:
    def decodeString(self, s: str) -> str:
        

        stack = []

        for c in s:
            print(stack)
            if c == "]":
                temp = ''
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                # pop of "["
                stack.pop()
                # pop the multiplier
                
                num = ""
                while stack and stack[-1].isnumeric():
                    num = stack.pop() + num

                temp = temp*int(num)
                stack.append(temp)
            else:
                stack.append(c)
        
        return "".join(stack)
