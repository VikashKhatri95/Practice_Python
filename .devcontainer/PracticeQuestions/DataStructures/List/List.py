#List are ordered,mutable collection of items.
lst=[]
print(type(lst))

names=["Vikash","jack","jaemison","Vyas"]
print(names)

mixed_bag=["one",1,2.33]
print(mixed_bag)

#Acessing List items
print(names[0])#first element
print(names[-1]) #Access Last element
print(names[1:])#all element from 1 to last position
print(names[-1:]) #['Vyas'] last element only
print(names[-1:-3])#[]

fruits=["Mango","grapes","pomegranate","kiwi","guava"]
fruits[0]="Stawberry"
print(fruits)
fruits[1:]={"watermellon"}
print(fruits)

#List Methods
fruits.append("orange")
print(fruits)
#insert an element
fruits.insert(1,"kiwi")
print(fruits)

fruits.remove("orange") #will give error if element is not present
print(fruits)

popped_fruits=fruits.pop() #remove element at index default last, error id list is empty.
print(fruits)

#returns index
index=fruits.index("kiwi")#error if not in list
print(index)

fruits.insert(4,"Apple")
print(fruits)

#count
print(fruits.count("banana")) #give count of banana

fruits.sort()
print(fruits)#asc order with priority to capital case

fruits.reverse() #reverse the list
print(fruits)

fruits.clear() #make the list empty
print(fruits)