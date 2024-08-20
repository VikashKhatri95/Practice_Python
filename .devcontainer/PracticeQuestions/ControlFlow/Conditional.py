## if statement evalutes the condition and execute the block of code id true
## else statement executes a block of code if the condition in the if statement is false
##elif allows to check for multiple statements

#Check for negative,odd,positive,even.
num=int(input("Enter a number: "))
if num>0:
    if num%2==0:
        print("Number is positive and Even")
    else:
        print("Number is positive and Odd")
else:
    print("The number is either 0 or negative")


# print(num1,end="") For printing without newline
