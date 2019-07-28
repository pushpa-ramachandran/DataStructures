# Tuple is a collection of Python objects much like a list.
# The sequence of values stored in a tuple can be of any type, and they are indexed by integers.
# The important difference between a list and a tuple is that tuples are immutable.
# Also, Tuples are hashable whereas lists are not.
# Tuples are immutable, and usually, they contain a sequence of heterogeneous elements
# that are accessed via unpacking or indexing (or even by attribute in the case of named tuples).
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

############ Slicing of a tuple ########################
#### Starting from an index

print('\n # # # Slicing a tuple - Starting from an index ')

tupel2 = ('str1',1,2,5.5,'g')

print('Original tuple :',tupel2)
print('tupel2[2:] --> ',tupel2[2:])

#### Slicing a tuple - Reversing the tuple

print('\n # # # Slicing a tuple - Reversing the tuple ')

tupel2 = ('str1',1,2,5.5,'g')

print('Original tuple :',tupel2)
print('tupel2[::-1] --> ',tupel2[::-1])

#### Starting ending -from to an index

print('\n # # # Slicing a tuple - Starting ending -from to an index ')

tupel2 = ('str1',1,2,5.5,'g')

print('Original tuple :',tupel2)
print('tupel2[2:4] --> ',tupel2[2:4])

############  Deleting a Tuple ############
# Tuples are immutable and hence they do not allow deletion of a part of it.
# Entire tuple gets deleted by the use of del() method.
# Printing of Tuple after deletion results to an Error.

#### Starting ending -from to an index

print('\n # # #  Deleting a Tuple ')

tupel2 = ('str1',1,2,5.5,'g')
print('Original tuple :',tupel2)

del tupel2
print('del tupel2 - tuple can not be accessed once deleted')

########### Other tuple functions #################################
# all()	Returns true if all element are true or if tuple is empty
# any()	return true if any element of the tuple is true. if tuple is empty, return false
# len()	Returns length of the tuple or size of the tuple
# enumerate()	Returns enumerate object of tuple
# max()	return maximum element of given tuple
# min()	return minimum element of given tuple
# sum()	Sums up the numbers in the tuple
# sorted()	input elements in the tuple and return a new sorted list
# tuple()	Convert an iterable to a tuple.