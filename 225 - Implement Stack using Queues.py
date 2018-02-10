class MyStack:

    a = []
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        print(self.a)
        self.a.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        print(self.a)
        return self.a.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        print(self.a)
        return self.a[len(self.a) - 1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        print(self.a)
        if len(self.a) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()