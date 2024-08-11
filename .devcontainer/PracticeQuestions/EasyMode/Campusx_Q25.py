#Write a program that can multiply 2 numbers provided by the user without using the * operator
def numMultiple(num1,num2):
    while(num1>0):
        num2=num2+1
        num1=num1-12
    return num2

num1=int(input("Enter first nmber: "))
num2=int(input("Enter second number: "))
print(f"Result={numMultiple(num1,num2)}")