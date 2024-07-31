class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        symbols = ["+", "-", "*", "/"]
        for i in tokens:
            if i in symbols:
                x = stack.pop()
                y = stack.pop()
                curr = 0
                if i == symbols[0]:
                    curr = x + y
                elif i == symbols[1]:
                    curr = y - x
                elif i == symbols[2]:
                    curr = x * y
                elif i == symbols[3]:
                    curr = int(float(y)/x)
                stack.append(curr)
            else:
                stack.append(int(i))
        return stack[-1]