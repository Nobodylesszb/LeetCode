# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class Minstack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self,x):
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)
    
    def pop(self):
        tmp = self.stack.pop()
        if tmp == self.minStack[-1]:
            self.minStack.pop()
    
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.minstackp[-1]