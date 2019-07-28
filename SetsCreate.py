####################     Set      #####################################################


# Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.
# Elements of a set can be added and deleted, elements of the set can be iterated,
# Various standard operations (union, intersection, difference) can be performed on sets.
# Set has a highly optimized method for checking whether a specific element is contained in the set.
# Order of elements in a set is undefined and is unchangeable.
# Type of elements in a set need not be the same, various mixed up data type values can also be passed to the set.
# A set cannot have mutable elements like a list, set or dictionary, as its elements.

############ Creating a set

### Creating a set - blank one
print('\n # # # Creating a set - blank one ')

set1 = set()

print(' set1 = set() ---->' ,set1)

### Creating a set - with a string passed
print('\n # # # Creating a set - with a string passed')

set1 = set("I will win")

print("I will win",' --->' ,set1)


### Creating a set - with a string OBJECT
print('\n # # # Creating a set - with a string OBJECT ')

str = "I will win"
set1 = set(str)

print(str,' --->' ,set1)


### Creating a set - with a list of strings
print('\n # # # Creating a set - with a list of strings ')

str = ["U will win","if U stay","focussed"]
set1 = set(str)

print(str,' --->' ,set1)

### Creating a set - with a list of integers
print('\n # # # Creating a set - with a list of integers ')

intList = [1,2,3,4,5]
set1 = set(intList)

print(intList,' --->' ,set1)

### Creating a set - with a list of integers - With DUPLICATES
print('\n # # # Creating a set - with a list of integers  - With DUPLICATES')

intList = [1,2,3,4,5,1,2,3,4,5]
set1 = set(intList)

print(intList,' --->' ,set1)


### Creating a set - with mixed types
print('\n # # # Creating a set - with mixed types')

mixed = [1,2,3,4,5,"confidence","focus","hardwork",100.00, 'i']
set1 = set(mixed)

print(mixed,' --->' ,set1)
