'''
Else clause is used with Try clause when you 
want to execute the set of instructions in the absence of exceptions in your code.

syntax:

try :
   print("")

except :
    print("")

else :
    print("")


'''

a=int(input("Enter the number :"))

try :
    if a % 2 == 0 :
        print(f"{b} is an even number")
    else:
        print(f"{b} is an odd number")
except Exception as e:
    print(e)
else:
    print("Else clause got executed")
 