class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        ops = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                x= stack.pop()
                y= stack.pop()
                if t == "+":
                    stack.append(y+x)
                elif t == "-":
                    stack.append(y-x)
                elif t == "*":
                    stack.append(y*x)
                elif t == "/":
                    stack.append(math.trunc(y/x))
        return stack[-1]