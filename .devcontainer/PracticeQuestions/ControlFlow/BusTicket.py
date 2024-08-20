#Determine the ticket price based on the age of the person.
try:
    age=int(input("Enter your age: "))
    is_student=input("Are you student?? {yes/No}").lower()
except ValueError:
    print("Enter a Valid Age!!!")

if(age<5):
    print("Free")
elif age<60 and is_student=="no":
    print("20")
else:
    print(10)