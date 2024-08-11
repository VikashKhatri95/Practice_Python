#sum of first n numbers
def sumOfnum(num):
    sum=0;
    sum=(num*(num+1))/2
    return sum

try:
    num=int(input("Enter a number to find the sum:"))
except ValueError:
    print("Error:Please enter a valid number")
result=sumOfnum(num)
print(f"Sum of first {num} numbers is {int(result)}")