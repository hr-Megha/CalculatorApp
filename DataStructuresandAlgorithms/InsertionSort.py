# Insertion Sort
'''
1. It is one of the easiest and brute force sorting algorithms.
2. Insertion sort is used to sort elements in either ascending or descending order
3. In Insertion sort, we maintain a sorted part and unsorted part
4. It works just like palying cards,i.e picking one card and sorting it with the cards that we have in our hand already
which in turn are sorted
5. with every iteration, one item from unsorted is moved to the sorted part 
6. First element is picked and considered as sorted.
7. Then we start picking from 2nd elements onwards and start comparing it with elements in sorted part.
8. we shift the elements from sorted by one element until an appropriate location is not found for the picked element.
9. This continues till all the elements get exhausted.

Best time complexity : O(n)
Averge time complexity : O(n^2)
worst time complexity  : O(n^2)

No auxiliary space is required in insertion sort implementation that 
is we are not using any arrays, linked list, stack, queue etc to store our elements 

Hence space complexity is O(1)


Insertion sort - Algorithm
Insertion Sort(arr,size)
consider 1st element as sorted part
for each element from i=2 to n-1
tmp=arr[i]
for j=i=1 to 0
 if a[j] > tmp
 then right shift it by one position
 put tmp at current j
'''
# Insertion sort implementation
def insertion_sort(array):
    for step in range(1,len(array)):
        key=array[step]
        j=step-1

        while j >=0 and key <array[j]:
            array[j+1]=array[j]
            j=j-1
            array[j+1]=key


data=[5,2,1,7,8]
insertion_sort(data)
print('Printed Array in Ascending order :')
print(data)


    