#Take a number and add the square of the numbers

def addSquare(num):
    temp=sum=0
    while(num>0):
        temp=num%10
        sum=sum+(temp)**2
        num=num//10
    return sum

number=int(input("Enter a number: "))
result=addSquare(number)
print(f"The Sum of Square of digits id {result}")