#Entered number is odd or even
def checkNumber(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")


number=int(input("Enter a number to find whether it is odd or even: "))
result=checkNumber(number)
