arr=[10.22,18,27,11]
temp=0

#Displaying elements of original array

print("Elements of original Array : ")
for i in range(0,len(arr)):
    print(arr[i],end= " ")

#sort the arrayin ascending order
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
         if(arr[i] > arr[j]):
             temp=arr[i]
             arr[i]=arr[j]
             arr[j]=temp
print()


    #Displaying elements of the array after sorting
print("Elements of array sorted in ascending order :")

for i in range(0,len(arr)):
        print(arr[i], end= " ")