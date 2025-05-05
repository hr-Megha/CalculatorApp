
print(end="Enter the size of the array :")
a=int(input())
arr=[]
print(end="Enter"+str(a) + "elements :" )

for i in range(a):
    arr.append(input())

print("ENter the value to Delete :")
val=input()
if val in arr:
    arr.remove(val)
    print("\n The new array is :")
    for i in range(a-1):
        print(end=arr[i] + " ")
else:
    print("\n Element does not exist in the List")