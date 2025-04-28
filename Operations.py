def add(a,b):    
    return print( 'Addition :', a+b)

def subtract(a,b):
    return print('Subtraction :', a-b)

def Multiplication(a,b):
    return print('Multiplication :' , a*b)

def Division(a,b):
    return print('Division : ', a/b)
    
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