print(range(5)) #range(0, 5)
for i in range(5):
    print(i,end=" ") # 0 1 2 3 4 

for i in range(5,20,2): #start,end,steps
    print(i)

for i in range(5,20,-1): #start,end,steps
    print(i)     #nothing will be printed

for i in range(10,1,-1):
    print(i)    #10,9,8...,3,2

#string is a collection of characters
str="Vikash Khatri"
for i in str:
    print(i)

#while loop continues to execute a piece of code untill the condition becoms false.
count=1
while count<5:
    print(count)
    count=count+1