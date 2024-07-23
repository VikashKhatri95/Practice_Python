#Reverse a four digit number
def reverseNumberFunction(num1):
    tempnum=reverseNumber=0
    while(num1>0):       
        tempnum=num1%10             
        reverseNumber=reverseNumber*10+tempnum
        num1=num1//10
    return reverseNumber
number=int(input("Enter a number: "))
result=reverseNumberFunction(number)
print(f"The reverse the number {result}")