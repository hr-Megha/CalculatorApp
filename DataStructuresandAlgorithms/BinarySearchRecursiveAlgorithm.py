# Binary Search  - Recursive Algorithm
'''
binarySearch(arr, item,beg, end)
if beg <= end
midIndex= (beg + end)/2

if item == arr[midIndex]
    return midIndex
else if arr[midIndex] > item 
    return binarySearch(arr,item,beg,midIndex-1)
else
    return binarySearch(arr,item,midIndex+1,end)
return -1


'''
