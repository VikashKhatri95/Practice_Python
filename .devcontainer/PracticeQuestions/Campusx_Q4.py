#Sum of 3 digits
def getsum(x):
    sum=0
    while(x):
        sum=sum+(x%10)
        x=x//10 # / always give float even if integer(division) // gives whole number (floor division)
    return sum

num=int(input("Enter a number: "))
number=getsum(num)
print(f"The Sum of the number is {number}")