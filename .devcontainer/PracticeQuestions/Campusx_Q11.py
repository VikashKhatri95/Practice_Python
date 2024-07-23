#Find SI with other parameters already provided
#SI=(Principle*Rate*Year)/100
def calculateInterest(principle,rate,year):
    return (principle*rate*year)/100

principle=float(input("Enter Principle "))
rate=float(input("Enter Rate "))
year=float(input("Enter Time in Years "))

result=calculateInterest(principle,rate,year)
print(f"The Interest on {principle} amount, after {year} at {rate} rate is {(result):.2f}")