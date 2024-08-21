l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

#List Comprehension-->offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Syntax --> newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[i for i in fruits if "a" in i]
print(newlist)

#Basic List comprehension

#for even numbers
list=[i for i in range(5) if i%2==0]
print(list)

for i in fruits:
    if "i" in i:
        print(i)

#Nested List Comprehension
list1=[1,2,3,4]
list2=['a','b','c','d']
pair=[[i,j] for i in list1 for j in list2]
print(pair)

#List comprehension with function calls
words=["hello","world","from","Comprehension","list"]
lengths=[len(word) for word in words] #length of each word
print(lengths)

