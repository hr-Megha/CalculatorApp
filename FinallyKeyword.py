# FInally is  a keyword which surely executes after the execution of thr try and except block of statment.
'''
try :
    print("")
except :
    print("")
else:
    print("")
finally:
    print("")

'''
a= int(input("ENter the first number :"))
b= int(input("Enter the second number :"))
try :
    if a>b : 
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")

except Exception as e:
        print(e)        
else :
     print("else clause got executed")

finally:
    print("Finally keyword used")