############ Accessing the list
print('\n # # # Accessing the list')

list = ['LIST4','LIST5','LIST6']

print(list)
print(list[2])


####### Accessing the multi dimensional list
print('\n # # # Accessing the multi dimensional list')

list = [['LIST4','LIST5','LIST6'],['LIST7','LIST8']]

print(list)
print('list[1] - ' ,list[1])
print('list[1][1] - ',list[1][1])

####### Accessing using NEGATIVE indexing
print('\n # # # Accessing using NEGATIVE indexing')

list = [['LIST4','LIST5','LIST6'],['LIST7','LIST8']]

print(list)
print('list[-1] - last element : ' ,list[-1])
print('list[-2] - second element from the last : ' ,list[-2])

################# Removing elements from the list
####### Remove() function
# Elements can be removed by using remove() function
# An Error arises if element doesn’t exist in the set.
# Remove() method only removes one element at a time
# To remove range of elements, iterator is used.
# Only removes the first occurrence of the searched element

####### Removing elements one at a time
print('\n # # # Removing elements one at a time')

for i in range(1,10):
    list.append(i*100)

print(list)

list.remove(500)
print('list.remove(500): ' , list)

####### Removing MULTIPLE elements by iterating
print('\n # # # Removing MULTIPLE elements by iterating')

for i in range(7,10):
    list.remove(i*100)

print('for i in range(7,10):  list.remove(i*100)): ' , list)

####### pop() function
# Pop() function can also be used to remove and return an element
# By default it removes only the last element of the set
# To remove element from a specific position of the List, index of the element is passed as an argument to the pop() method.

####### Removing by using pop() - no index passed. Removes the last element
print('\n # # # Removing by using pop() - no index passed. Removes the last element')

list.pop()

print('After list.pop()): ' , list)

####### Removing by using pop() -  index passed. Removes the element at the index
print('\n # # # Removing by using pop() -  index passed. Removes the element at the index')

list.pop(1)

print('After list.pop(1)): ' , list)


### Funcitons list
# Append()	Add an element to the end of the list
# Extend()	Add all elements of a list to the another list
# Insert()	Insert an item at the defined index
# Remove()	Removes an item from the list
# Pop()	    Removes and returns an element at the given index
# Clear()	Removes all items from the list
# Index()	Returns the index of the first matched item
# Count()	Returns the count of number of items passed as an argument
# Sort()	Sort items in a list in ascending order
# Reverse()	Reverse the order of items in the list
# copy()	Returns a copy of the list