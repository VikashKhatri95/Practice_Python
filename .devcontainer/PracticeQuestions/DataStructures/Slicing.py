#Slicing List
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])

print(numbers[:5]) #print start to 5th element
print(numbers[::2])# print every 2nd number
print(numbers[::-1]) #reverse the list 

#itearation over list
for i in numbers:
    print(i)

for index,number in enumerate(numbers):
    print(index,number)