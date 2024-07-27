#Give inhand Salary after deduction HRA(10%),DA(5%),PF(3%) and if salary in between 5-10(10%)
def calculateSal(salary):
    if(salary>500000 and salary<1000000):
        inhand=salary*0.9+salary*0.95+salary*0.97+salary*0.9
    elif(salary>1100000 and salary<2000000):
        inhand=salary*0.9+salary*0.95+salary*0.97+salary*0.8
    elif(salary>2000000):
        inhand=salary*0.9+salary*0.95+salary*0.97+salary*0.7
    else:
        inhand=salary*0.9+salary*0.95+salary*0.97+salary*0.9
    return inhand
salary=float(input("Enter your Salary: "))
inhand=calculateSal(salary)
print(f"Your Inhand Salary After Deduction of Taxes is {inhand}") #None if we did not return the value from function