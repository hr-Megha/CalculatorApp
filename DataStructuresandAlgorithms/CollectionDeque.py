# stacks in python are created by the collection module which provides deque class
# append and pop operations are faster in deque as compare to list 

# Logic
# from collections import deque 
#  stack= deque()
#  stack.append("abc")
#  print(stack.pop())

#Implementation using Deque

from collections import deque
stack=deque()
stack.append('x')
print(stack)
stack.append('y')
print(stack)
stack.append('z')
print(stack)
stack.pop()
print(stack)

# only the thing is Deque is faster than list because pop and append functions are faster in deque 
