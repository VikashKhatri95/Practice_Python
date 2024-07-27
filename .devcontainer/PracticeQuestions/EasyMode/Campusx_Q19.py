#Check for Narcissist Number
def isNarcissist(number):
    copy_num=tempnum=number
    sum=count=0
    while(tempnum>0):
        tempnum=tempnum//10
        count=count+1
    while(number>0):
        temp=number%10
        sum=sum+temp**count
        number=number//10
    if(copy_num==sum):
        result=True
    else:
        result=False
    return result

number=int(input("Enter a Number: "))
result=isNarcissist(number)
if(result==True):
    print(f"{number } is an Narcissist number")
else:
    print("Not an Narcissist Number")