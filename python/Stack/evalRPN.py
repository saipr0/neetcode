class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '-':
                stack.append(-stack.pop() + stack.pop())
            elif t == '/':
                divisor = stack.pop()
                stack.append(int(stack.pop() / divisor))
            else:
                stack.append(int(t))
        return stack.pop()

# Test
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(int(3/4))
