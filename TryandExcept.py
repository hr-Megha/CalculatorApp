# TRY AND EXCEPT STATEMENT
'''
1. The code written inside the try block executes if the code is error free
2.if the code is not error free then the Except block gets executed and results an exception.
3.A try statement can have more than mone except statement.

syntax:

try:
    statement
except:
    Exception

'''

a=input("enter the first number :")
b=input("enter the second Number :")

try:
    c=int(a)+int(b)
    print(c)


except Exception as e:
    print("error in the try block")