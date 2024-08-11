#Write a program that can find the factorial of a given number provided by the user.

def factorial(num):
    fact=1
    while(num>0):
        fact=fact*num
        num=num-1
    return fact

try:
    num=int(input("Enter a num to find factorial: "))
except ValueError:
    print("Enter a valid number")
result=factorial(num)
print(f"The result is {result}")