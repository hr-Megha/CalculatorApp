'''
Linear Data Structure
Contiguous memory locations
Access elements randomly 
Homogeneous elements i.e similar elements
Arrays
Stack
Queue
Linked List
Linear Search
Binary Search
Insertion Sort
Quick Sort
Merge Sort

'''
# one dimensional

print("how many elements to store inside the array :", end="")

num= input()
arr=[]
print("Enter", num , "Element :", end="")
num =int(num)
for i in range(num):
    element=input()
    arr.append(element)
    print("\nThe array elements are")
for i in range(num):
        print (arr[i], end="")