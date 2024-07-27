#Check for Armstrong number
def isArmstrong(number):
    copy_num=number
    sum=0
    while(number>0):
        temp=number%10
        sum=sum+temp**3
        number=number//10
    if(copy_num==sum):
        result=True
    else:
        result=False
    return result

number=int(input("Enter a Number: "))
result=isArmstrong(number)
if(result==True):
    print(f"{number } is an armstrong number")
else:
    print("Not an Armstrong Number")