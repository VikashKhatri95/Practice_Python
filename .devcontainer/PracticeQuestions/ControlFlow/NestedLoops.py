# for i in range(3):
#     for j in range(2):
#         print(f"i={i},j={j}")

#Calculate the sum of n natural number using for and while loop
# sum=0
# n=int(input("Enter n to find sum till n: "))
# while(n>0):
#     sum=sum+n
#     n=n-1
# print(f"Sum= {sum}")

# for i in range(n+1):
#     sum=sum+i
# print(sum)

#prime number between 1 and 100
for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)