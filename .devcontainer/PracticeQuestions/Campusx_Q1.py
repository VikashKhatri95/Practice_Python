#Code tht will input 3 ages and find the oldest one.
flag = 1
while(flag):
    ageofp1 = int(input("Age of person 1: "))
    ageofp2 = int(input("Age of person 2: "))
    ageofp3 = int(input("Age of person 3: "))
    
    if ageofp1 >= ageofp2 and ageofp1 >= ageofp3:
        print(f"Person 1 is the oldest, age = {ageofp1}")
    elif ageofp2 >= ageofp1 and ageofp2 >= ageofp3:
        print(f"Person 2 is the oldest, age = {ageofp2}")
    else:
        print(f"Person 3 is the oldest, age = {ageofp3}")
    
    flag = int(input("Want to check more ages? (1/0): "))
