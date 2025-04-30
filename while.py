# while - keep filling the bucket with a mug of water  while it is not full

fruits=["apple","banana","mango"]

for i in fruits:
    print(i)

# nested for loop

color=["blue","green","yellow"]
item=["book","ball","chair"]

for i in color:
        for j in item:
            print(i,j)

# while loop

i= 1

while i <=10:
     print(i)
     i+=1

# while with List
l1=[1,2 ,3 ,4]
i=0

while i < len(l1):
     l1[i]=l1[i]+100
     print(l1)
     i+=1