#Number divisible by 3 &6

def checkDivisible(num):
    if(num%2==0 and num%3==0):
        print("Number is divisible by 3 and 6")
    else:
        print("Number is not divisible by 3 and 6")

try:
    number=int(input("Enter a number to check Divisibility by 3 and 6 "))
    checkDivisible(number)
except ValueError:
    print("Enter Valid Number")