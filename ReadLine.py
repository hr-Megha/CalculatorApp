''' 1.The readline function helps us to read the text line by line 
    2.For using this function, firstly open file is needed and whatever 
    way you want you can open the file, either read or write
    3.Then accordingly use the readiline function to read the lines accordingly in the form of line by line

  '''
#readline
f=open("hello.txt","r")
# f.write("I am learning file handling \n")
# f.write("\nTopics are open, read  and write mode \n")
# f.write("\nappend function")
print(f.readline())
print(f.readline())     #each line in text file reads separately
print(f.readlines())    # there are 3 lines in hello.txt file, readline() reads each line per run the command while readlines reads every line at a time.
f.close()