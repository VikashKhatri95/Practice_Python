#Write a program to print the first 25 odd numbers

def oddNums(count):
    result=1
    while(count>0):
        print(f"{result}")
        result=result+2
        count=count-1

count=int(input("Enter count to display odd numbers: "))
oddNums(count)