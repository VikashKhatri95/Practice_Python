#Tuples are oredred collection of items that are immutable.
empty_tuple=()
print(empty_tuple)
print(type(empty_tuple))

#Convert list to tuples
numbers=tuple([1,2,3,4,5])
print(numbers)

#Tuple to list
num1=list((1,2,3,4,5))
print(num1)

# Creating a mixed tuple
mxd_tuple = (1, "Hello", 2.5)
print(mxd_tuple)

# Accessing tuple elements
tpl = ('1', 2, 3, 4)
print(tpl[1])

# Concatenating tuples
concattuple = tpl + mxd_tuple
print(concattuple)
