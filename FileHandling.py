# File handling
''' 
1.Dealing with text files is known as File Handling  or even called as  File I/O functions.
2.There are different functions involved , which helps to read, write , append,alter and perform many other functions.
Open , read and write Modes.

3. -->Open Mode: This mode is Used whenever you want to open your text file for reading ,writing or doing some other stuffs
   -->Read Mode: This mode is used whenever you want to read the text which is already stored in your text file.
   -->write mode : this mode is used whenever you want to write in your text file that is .txt file.
'''

f= open("test.txt","w") # to write "w"
f.write("Hello World! Welcome to Python File Handling")

f=open("test.txt","r")  #to write "r"  once the file is open for write then only we can read
content=f.read()
print("File Content",content)


k=open("demo.txt","w")
k.write("I am learning file handling")
f.close()   #its good practice to close once it is done


