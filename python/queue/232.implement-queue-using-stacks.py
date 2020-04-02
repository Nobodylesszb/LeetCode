"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

"""
"""
The idea is to simulate a queue 
using two stacks (same as previous posts). 
I use python list as the underlying data structure for stack 
and add a "move()" method to simplify code: 
it moves all elements of the "inStack" to the "outStack" when the "outStack" is empty. Here is the code
"""

class Queue:
    def __init__(self):
        self.inStack,self.outStack = [],[]

    def push(self,x):
        self.inStack.append(x)
    
    def pop(self):
        self.move()
        self.outStack.pop()
    
    def peek(self):
        self.move()
        return self.outStack[-1]

    def empty(self):
        return (not self.inStack) and (not self.outStack)
    
    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
