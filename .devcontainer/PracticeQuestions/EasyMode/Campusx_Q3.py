#Program to swap two numbers.
def swap(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Number before Swapping:")
print("first number: {0} second number: {1}".format(num1, num2))
num1, num2 = swap(num1, num2)
print("Number after Swapping:")
print("first number: {0} second number: {1}".format(num1, num2))

