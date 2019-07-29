# values() is an inbuilt method that returns a list of all the values available in a given dictionary.
######### Accessing values - using values()
print('\n # # # Accessing values - using values() ')

dict1 = {0: 'zero', 1: 'one'}
dict1.update({1:'oness' , 4: 'four'})

dict2 = {'mark1' : 80 , 'mark2' : 88 , 'mark3' : 90}

print('dict1.values() --->' , dict1.values())
print('sum of all the marks- sum(dict2.values()) ---> ', sum(dict2.values()))

############## Removing Elements from Dictionary #################
# Deletion of keys can be done by using the del keyword.
# Using del keyword, specific values from a dictionary as well as whole dictionary can be deleted.
# Other functions like pop() and popitem() can also be used for deleting specific values and arbitrary values from a Dictionary.
# All the items from a dictionary can be deleted at once by using clear() method.
# Items in a Nested dictionary can also be deleted by using del keyword and providing
# specific nested key and particular key to be deleted from that nested Dictionary.
# del Dict will delete the entire dictionary and hence printing it after deletion will raise an Error.

######### Deleting values - using del dictionaryName
print('\n # # # Deleting values - using del dictionaryName ')

dict1 = {0: 'zero', 1: 'one'}
dict1.update({1:'oness' , 4: {41: 'four1', 42: 'four2'}}) # Nested dictionary

dict2 = {'mark1' : 80 , 'mark2' : 88 , 'mark3' : 90}

# del
print('### Before deleting ', dict1)
del dict1[0]
print('del dict1[0] --->' ,dict1 )

print('### Before deleting ', dict1)
del dict1[4][42]
print('del dict1[4][42] ---> ', dict1)


######### Deleting values - using pop(key)
print('\n # # # Deleting values - using pop(key)  ')

dict1 = {0: 'zero', 2: 'two', 1: 'one'}
dict1.update({1:'oness' , 4: {41: 'four1', 42: 'four2'}}) # Nested dictionary

dict2 = {'mark1' : 80 , 'mark2' : 88 , 'mark3' : 90}

# pop()
print('### Before popping ', dict1)
dict1.pop(1)
print('dict1.pop(1)) --->' ,dict1 )

######### Deleting values - using popitem() - Deletes an arbitrary item
print('\n # # # Deleting values - using popitem  ')

dict1 = {0: 'zero', 2: 'two', 1: 'one'}
dict1.update({1:'oness' , 4: {41: 'four1', 42: 'four2'}}) # Nested dictionary

dict2 = {'mark1' : 80 , 'mark2' : 88 , 'mark3' : 90}

# pop()
print('### Before popping ', dict1)
dict1.popitem()
print('dict1.popitem() --->' ,dict1 )

######### Deleting an entire dictionary - using clear()
print('\n # # # Deleting an entire dictionary - using clear()  ')

dict1 = {0: 'zero', 2: 'two', 1: 'one'}
dict1.update({1:'oness' , 4: {41: 'four1', 42: 'four2'}}) # Nested dictionary

# clear()
print('### Before clearing ', dict1)
dict1.clear()
print('dict1.clear() --->' ,dict1 )

# copy()	They copy() method returns a shallow copy of the dictionary.
# clear()	The clear() method removes all items from the dictionary.
# pop()	Removes and returns an element from a dictionary having the given key.
# popitem()	Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
# get()	It is a conventional method to access a value for a key.
# dictionary_name.values()	returns a list of all the values available in a given dictionary.
# str()	Produces a printable string representation of a dictionary.
# update()	Adds dictionary dict2’s key-values pairs to dict
# setdefault()	Set dict[key]=default if key is not already in dict
# keys()	Returns list of dictionary dict’s keys
# items()	Returns a list of dict’s (key, value) tuple pairs
# has_key()	Returns true if key in dictionary dict, false otherwise
# fromkeys()	Create a new dictionary with keys from seq and values set to value.
# type()	Returns the type of the passed variable.
# cmp()	Compares elements of both dict