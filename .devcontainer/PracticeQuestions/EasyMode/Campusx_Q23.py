#Swap Numbers

def swapnum(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    return num1,num2

try:
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
except ValueError:
    print("Error:Enter a valid number")
print(f"Numbers Before Swapping {num1} and {num2}")
num1,num2=swapnum(num1,num2)
print(f"Numbers after swapping: {num1} and {num2}")