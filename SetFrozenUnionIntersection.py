###############     Frozen sets ############################
# Immutable objects that only support methods and operators
# that produce a result without affecting the frozen set or sets to which they are applied.
# While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
# If no parameters are passed, it returns an empty frozenset.

### Creating a frozen set - frozenset()
print('\n# # # Creating a frozen set - frozenset() ')

str = {'a','b','c','d'}
set1 = frozenset(str)
print(set1)


### Empyting a frozen set - frozenset()
print('\n# # # Empyting a frozen set - frozenset() ')

set1 = frozenset()
print(set1)

### Intersection of a sets - set1 & set2
print('\n# # # Intersection of a sets - set1 & set2  ')

set1 = {x*10 for x in range(1,10) if x > 5}
print('set1 ----> ', set1)


set2 = {x*10 for x in range(3,15) if x >6 }
print('set2 ----> ', set2)

print("Intersection set1 & set 2 ---- >", set1 & set2)


### Union of a sets - set1 | set2
print('\n# # #Union of a sets - set1 | set2  ')

set1 = {x*10 for x in range(1,10) if x > 5}
print('set1 ----> ', set1)


set2 = {x*10 for x in range(3,15) if x >6 }
print('set2 ----> ', set2)

print("Union of a sets - set1 | set2 ---- >", set1 | set2)



# add()	Adds an element to a set
# remove()	Removes an element from a set. If the element is not present in the set, raise a KeyError
# clear()	Removes all elements form a set
# copy()	Returns a shallow copy of a set
# pop()	Removes and returns an arbitary set element. Raise KeyError if the set is empty
# update()	Updates a set with the union of itself and others
# union()	Returns the union of sets in a new set
# difference()	Returns the difference of two or more sets as a new set
# difference_update()	Removes all elements of another set from this set
# discard()	Removes an element from set if it is a member. (Do nothing if the element is not in set)
# intersection()	Returns the intersection of two sets as a new set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# symmetric_difference()	Returns the symmetric difference of two sets as a new set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another