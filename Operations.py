def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    return a/b
    
print("Select Operation: +, -, % , *")
choice = input("Enter choice: ")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number : "))

if(choice == '+'):
    add(num1,num2)
elif(choice=='-'):
    subtract(num1,num2)
elif(choice=='*'):
    Multiplication(num1,num2)
elif(choice=='%'):
    Division(num1,num2)
else: 
    print("Invalid Input")