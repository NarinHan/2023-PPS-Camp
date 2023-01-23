'''
    A088 Min Stack
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
    https://leetcode.com/problems/min-stack/
'''

class MinStack(object):
    stack = list()

    def __init__(self):
        self.stack = list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """  
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)