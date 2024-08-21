#Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
list1=[i**2 for i in range(11)]
# print(list1)

#Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
lst=[i for i in range(1,21)]
evenlist=[i for i in lst if i%2==0]
# print(evenlist)

#Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
import random
randomList=[]
for i in range(5):
    randomList.append(random.randint(2,5))
randomList.sort(reverse=True)
print(randomList)
unique_numbers = list(set(randomList))
print(unique_numbers)