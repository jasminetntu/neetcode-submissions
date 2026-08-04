class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # first 2 must always be numbers, not operands

        import math

        # if len(tokens) == 1:
        #     return int(tokens[0])

        stack = []

        for i in range(0, len(tokens)):
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
