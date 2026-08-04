class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if len tokens > 1, first 2 must always be numbers, not operands

        import math

        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = [int(tokens[0]), int(tokens[1])]

        for i in range(2, len(tokens)):
            # print(stack)
            if tokens[i] == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif tokens[i] == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif tokens[i] == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif tokens[i] == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                if (num1 / num2) < 0:
                    stack.append(math.ceil(num1 / num2))
                else:
                    stack.append(math.floor(num1 / num2))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]
