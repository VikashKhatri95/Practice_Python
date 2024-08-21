#Create a list of the first 20 positive integers. Print the list.
lst=[i for i in range(1,21)]
# print(lst)

#Print the first, middle, and last elements of the list created in Assignment 1.

print(lst[0],lst[len(lst)//2],lst[-1])

#Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
print(lst[:5])
print(lst[5:15])
print(lst[-5:])