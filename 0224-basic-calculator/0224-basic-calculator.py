class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        current_number = 0
        sign = 1  # 1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            elif char == '+':
                # Evaluate the expression to the left
                result += sign * current_number
                # Reset for the next number
                sign = 1
                current_number = 0
                
            elif char == '-':
                # Evaluate the expression to the left
                result += sign * current_number
                # Reset for the next number
                sign = -1
                current_number = 0
                
            elif char == '(':
                # We are starting a new sub-expression.
                # Push the current result and sign onto the stack.
                stack.append(result)
                stack.append(sign)
                # Reset the state for the new sub-expression.
                result = 0
                sign = 1
                
            elif char == ')':
                # Evaluate the last number in the sub-expression.
                result += sign * current_number
                
                # The sub-expression is done. Merge it with the outer expression.
                # Pop the sign that was before the '('.
                result *= stack.pop() 
                # Pop the result from before the '('.
                result += stack.pop()
                
                # Reset the number for the next part of the expression.
                current_number = 0

        # Add the last unprocessed number to the result.
        return result + sign * current_number