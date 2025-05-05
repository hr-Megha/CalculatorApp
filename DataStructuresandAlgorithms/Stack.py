# Linear data structure
# It follows last in first out  (LIFO) order
# Insertion and removal of the element has done at one end
# Push is used for inserting an element in a stack 
# Pop is used to removal an element in a stack.
# Functions associated with Stack
# 1.push(x) - it is used to insert the element 'x' at the end of stack.
# 2.pop() - It is used to remove the topmost/last element of a stack.
# 3.size() - gives the size / length of a stack
# 4.top() - give reference of last element present in stack
# 5.empty() - returns true for an empty stack

#       Implementation of Stack
# 1.list
# 2.Collections.deque
# 3.queue.LifoQueue

# List in Python can be used as stack  - it LIFO order 

stack =[]
stack.append("Welcome")
stack.append("to")
stack.append("Python")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())