# Tuple is a collection of Python objects much like a list.
# The sequence of values stored in a tuple can be of any type, and they are indexed by integers.
# The important difference between a list and a tuple is that tuples are immutable.
# Also, Tuples are hashable whereas lists are not.
# Tuples are immutable, and usually, they contain a sequence of heterogeneous elements
# that are accessed via unpacking or indexing (or even by attribute in the case of named tuples).
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

########## Creating a tuple ###################

# Tuples are created by placing sequence of values separated by ‘comma’ with or without the use of parentheses for grouping of data sequence.
# Tuples can contain any number of elements and of any datatype (like strings, integers, list, etc.)
# Tuples can also be created with a single element, there must be a trailing ‘comma’ to make it a tuple.
#
# Creation of Python tuple without the use of parentheses is known as Tuple Packing.


############ Creating a tuple with strings
print('\n # # # Creating a tuple with strings')

tupel1 = ('Creating', 'a' ,'tuple', 'with' ,'strings')

print(tupel1)


############ Creating a tuple with list of integers using tuple()
print('\n # # # Creating a tuple with list of integers using tuple()')

list = [1,2,3,4,5]
tupel2 = tuple((list))

print(tupel2)


############ Creating a tuple with mixed datatypes
print('\n # # # Creating a tuple with mixed datatypes')

tupel2 = ('str1',1,2,5.5,'g')

print(tupel2)

############ Creating a nested tuple
print('\n # # # Creating a nested tuple ')

tupel2 = ('str1',1,2,5.5,'g')
tupel3 = ("creating","nested","tuples")

tupleNested = (tupel2 , tupel3)

print(tupel2)
print(tupel3)
print('tupleNested = (tupel2 , tupel3) ---> ', tupleNested)

############ Creating a tuple concatenating 2 tuples
print('\n # # # Creating a nested tuple ')

tupel2 = ('str1',1,2,5.5,'g')
tupel3 = ("creating","nested","tuples")

tuplesConcatenated = tupel2 + tupel3

print(tupel2)
print(tupel3)
print('tuplesConcatenated = tupel2 + tupel3 ---> ', tuplesConcatenated)

############ Creating a tuple with repetition
print('\n # # # Creating a tuple with repetition ')

tupel2 = ('str1',1,2,5.5,'g') * 2

print(tupel2)