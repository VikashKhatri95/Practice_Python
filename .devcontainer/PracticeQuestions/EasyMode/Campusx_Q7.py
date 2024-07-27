#Leap year or not
def checkLeapYear(year):
    if((year%4)==0 or year%400==0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
        
year=int(input("enter a year to find whether it is leap year or not: "))
checkLeapYear(year)