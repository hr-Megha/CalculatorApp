# Queue module contains LIFO queue.
# It is having some additional functions and works same as stack.
# put function is used to insert the data in queue.
# get function is used to remove the element

# Functions available in the Queue module
#  get() - It is used to remove the element from the queue. ---> remove the element
#  maxsize() - used to put the maximum number of items allowed in queue. 
#  empty() - It returns true, when queue is empty else false.
#  full() - when queue is full returns True.
#  put(x) - It is used to insert x in queue.  ------> insert the element
#  qsize() - gives the size of a queue.

#  Logic

# stack Implementation using queue
from queue import LifoQueue
stack=LifoQueue(maxsize=4)    # size here we declared is 3 
stack.put(2)
stack.put(3)
stack.put(4)
print(stack)
print(stack.qsize())
stack.get()           # to remove from stack
print(stack.full())   # when max size is 3  full() --> true suppose maxsize is 4  full() it gives false.
