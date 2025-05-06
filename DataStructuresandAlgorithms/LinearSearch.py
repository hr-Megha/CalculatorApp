'''
Linear Search Algorithm

It helps you to search for an element in a linear data structure.
It checks  each and every element for the element to be searched. 
Since this is done in linear fashion, it is termed as linear search.

linearSearch(arr,item)
for each element in the array
    if item==element
        return its index 
return -1


No auxiliary space is required in Linear Search implementation
Hence Space complexity is : O(1)
'''
#Linear Search Implementation

array=[2,4,0,1,9]
x=5
n=len(array)

def linearSearch(array, n, x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1

result= linearSearch(array,n,x)

if (result == -1) :
    print("Element not found")

else:
    print("Element found at index : ",result)
