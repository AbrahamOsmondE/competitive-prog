class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        if (len(self.stack) == 0):
            self.stack.append([val, val])
        else:
            self.stack.append([val, min(self.stack[-1][-1], val)])
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][-1]
        