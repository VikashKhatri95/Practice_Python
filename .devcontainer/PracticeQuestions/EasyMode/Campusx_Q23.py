#Swap Numbers

def swapnum(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    return num1,num2

num1=int(input("Enter 1st number: "))
num2=int(input("Enter second number: "))
num1,num2=swapnum(num1,num2)