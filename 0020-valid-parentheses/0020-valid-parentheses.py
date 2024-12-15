# 
class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {'{': '}', '[': ']', '(': ')'}
        
        if len(s) % 2 == 1:
            return False
        
        stack = []
        for char in s:
            if char in bracks:  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                if not stack or bracks[stack[-1]] != char:  # Mismatch or empty stack
                    return False
                stack.pop()  # Remove matched opening bracket
        
        return not stack  # Valid if stack is empty
