k=open("demo.txt","w")
k.write("I am learning file handling")
k.close()   #its good practice to close once it is done


'''
Adding text,counting characters
1.Append function helps us to add the text in your .txt file
2.The mode used is 'a'for appending means adding or writing some text to the file
3.For adding text to the file in a new line use \n before writing the sentence to be added.

len() function

1.To count the characters in a text file len() is the function used.
2. firstly we open the file and read that using functions
3.And after that reading of the text len function is assigned  with the variable  to find the count of characters

'''

#append
w=open("file.txt","a")
w.write("\n This is an \n append function \n")  # it will append the text how many times it gets execute
print(w)
w.close()

#len()
r=open("demo.txt","r")
data_read=r.read()
total_count=len(data_read)
print(total_count)

y=open("super.txt","w")
x=y.write("Hi Hello How are you doing")
z=open("super.txt","r")
o=z.read()
tot_count=len(o)
print(tot_count)
z.close()
y.close()