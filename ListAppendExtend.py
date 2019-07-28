#################   List   ########################

# General purpose, Most widely used data structure.
# Sequence type
# Sortable
# Lists need not be homogeneous always which makes it a most powerful tool in Python.
# A single list may contain DataTypes like Integers, Strings, as well as Objects.
# Lists are mutable, and hence, they can be altered even after their creation.
# Grow and shrink size as needed

############Creating a list

#Blank list
print('#Blank list')
list =[]
print(list)

#List with a string
print('#List with a string')
list =['#List with a string']
print(list)

#Homegeneous list - with repetetive elements
print('#Homegeneous list - with repetetive elements')
list =[1,3,2,1,5,6]
print(list)

# Non Homogeneous List
print('# Non Homogeneous List')
list =[1, 'one',2,'two']
print(list)

# List of Lists - Multi dimentional Lists
print('# List of Lists - Multi dimentional Lists')
list =[1,1,[2,3],"one",["any","text"]]
print(list)

##################   Adding to the list
############# Append

# Only one element at a time can be added to the list
# For addition of multiple elements with the append() method, use loops.
# Tuples can also be added to the List with the use of append method because tuples are immutable.
# Unlike Sets, Lists can also be added to the existing list with the use of append() method.

# Append elements one by one
print('# Append elements one by one')
list =[1,1,[2,3],"one",["any","text"]]
print(list)

print('Appending 6,7,8 one by one')
list.append(6)
list.append(7)
list.append(8)

print('\n After adding new elements')
print(list)

# Using for loop to append many elements
print('\n # Using for loop to append many elements')

for i in range (1,10,1):
    list.append(i*10)

print(list)


# Adding tuple (100,200) to the list
print('\n # # Adding tuple (100,200) to the list')

list.append((100,200))

print(list)

# Adding list ['LIST3', 'LIST4'] to the list
print('\n # # # Adding list [\'LIST3\', \'LIST4\'] to the list')

listToBeAdded = ['LIST3','LIST4']
list.append(listToBeAdded)

print(list)

############ Insert - To add an element at a SPECIFIC position
print('\n # # # Insert - To add an element at a SPECIFIC position')

listToBeInserted = ['LIST1','LIST2']
positionToBeInserted = len(list)-1 #last but one position

list.insert(positionToBeInserted,listToBeInserted)

print(list)


############ Extend - To add MULTIPLE elements at the END of a list
print('\n # # # Extend - To add MULTIPLE elements at the END of a list')

listToBeExtended = ['LIST5','LIST6']
list.extend(listToBeExtended)

print(list)