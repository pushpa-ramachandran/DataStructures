########################   Add elements to a set ############################

# Elements can be added to the Set by using built-in add() function.
# Only one element at a time can be added to the set by using add() method
# Loops are used to add multiple elements at a time with the use of add() method
# Whereas for addition of two or more elements Update() method is used.
# The update() method accepts lists, strings, tuples as well as other sets as its arguments.
# In all of these cases, duplicate elements are avoided.
# Lists cannot be added to a set as elements because Lists are not hashable
# Whereas Tuples can be added because tuples are immutable and hence Hashable.



### Adding elements to a set - add() one at a time
print('\n # # # Adding elements to a set - add()')

set1 = set()
set1.add(1)

print(' set1 = set(); set1.add(1)',' --->' ,set1)


### Adding elements to a set - add() multiple elements in a loop
print('\n # # # Adding elements to a set - add() multiple elements in a loop')

set1 = set()
for i in range (1, 10,1):
    set1.add( i *10)

print(' set1.add( i *10)',' --->' ,set1)

### Adding tuple to a set
print('\n # # # Adding tuple to a set ')

tuple = (1,2,3)
set1.add(tuple)

print('set1.add(tuple)',' --->' ,set1)

### Adding multiple elements to a set using update()
print('\n # # # Adding multiple elements to a set using update() ')

set1.update([100,200])

print('set1.add(tuple)',' --->' ,set1)

