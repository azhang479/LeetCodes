class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        #I'm thinking use 2 stacks, one for number and one for operator
        #Actually 1 for numbers should be fine, then just pull 2 when there is an operator
        #Basically, all numbers go in stack. When we read an operator, pull the top 2 and do the operation. Then, push number back on stack.
        #Eventually, we should be left with 1 number which will be our answer.
        #All operations are b x a
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                elif token == "/":
                    stack.append(int(b / a))
            else:
                stack.append(token)
        return int(stack[0])