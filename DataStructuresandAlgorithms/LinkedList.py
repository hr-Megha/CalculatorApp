# It is a collection or group of nodes
# Each node contaims data and reference (pointer) which contains the address of next node.
# It is a linear data structure
# Elements are stored randomly in memory.

# Why Linked LIst?
'''
>> Linked list is having more efficiency for performing the operations as compared to list
>> Elements are stored randomly whereas in list at contiguous memory
>> Accessing the elements in linked list will be slower as compare to list
>> Utilization of memory is higher than the list.
 each node has data and reference
 access of node is very slow in linked list

 Singly Linked List   
 >> It traverse only in one direction.

 Operations on Singly Linked List
 Several operations that can be performed are...
 Insertion  -Begining -At Specified node -End
 Deletion   -Begining -At Specified node -End
 Traversal - Going through each node of the linked list

'''
#Pseudo Code
#Creating a Node in Singly Linked List
class Node:

    def __init__(self,data):
        self.data=data
        self.reference=None

node1=Node(3)
print(node1.data)
print(node1.reference)

# Creating a Node in Singly Linked List

class LinkedList:
    def __init__ (self):
        self.head=None  # head is equal to none means it not connected to any other node
        print("Hi ")
sll=LinkedList()   #sll.head=None