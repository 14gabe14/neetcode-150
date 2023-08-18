class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        
        for i in range(len(tokens)):
            if tokens[i] == "+":
                last = stack.pop()
                first = stack.pop()

                stack.append(first + last)
            elif tokens[i] == "-":
                last = stack.pop()
                first = stack.pop()

                stack.append(first - last)
            
            elif tokens[i] == '*':
                last = stack.pop()
                first = stack.pop()

                stack.append(first * last)
            
            elif tokens[i] == "/":
                last = stack.pop()
                first = stack.pop()

                stack.append(int(first / last))

            else:
                stack.append(int(tokens[i]))

        return stack[-1]
