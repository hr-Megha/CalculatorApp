# Binary Search Algorithm
''' 
Binary search is one of the searching techniques
It can be used on sorted array
This searching technique follows 
the divide and conquer strategy and search space always reduce to half in every iteration.
This is very efficient technique for searching but it needs some order on which partition of the array will occur.

Space Complexity 
No auxiliary space is required in Binary Search implementation
Hence space complexity is : O(1)

Binary Search - Iterative Algorithm
binarySearch(arr, size)
loop until beg is not equal to end
midIndex=(beg + end)/2
if(item== arr[midIndex])
    return midIndex
elif (item > arr[midIndex])
    beg=midIndex + 1
else
    end=midIndex -1
'''

def binarySearch(array,x,low,high): # 9 0 6
    while low <= high:    # 0 <= 6

        mid=low + (high - low)//2  #0 + (6-0)/2  -- 3
        
        if array[mid] == x:  
            return mid
        
        elif (array[mid] < x):
            
            low = mid + 1
        else :
            high = mid - 1

    return -1

array=[3,4,5,6,7,8,9]
x=9
result=binarySearch(array,x,0,len(array)-1)

if (result != -1):

    print("Element is present at index : "+ str(result))
else:
    
    print("Element not found")