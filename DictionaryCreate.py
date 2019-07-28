####################     Dictionary           ##################
# Dictionary holds key:value pair. Each key-value pair is separated by a colon :, whereas each key is separated by a ‘comma’.
# Keys of a Dictionary must be unique and of immutable data type such as Strings, Integers and tuples,
# but the values can be repeated and be of any type


################# Creating a dictionary
# Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable.
# Dictionary can also be created by the built-in function dict().
# Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.

### Creating an Empty dictionary and creating with interger keys
print('\n# # #Creating an Empty dictionary) and creating with interger keys ')

dict1 = {}
print('Empty ' ,dict1)

dict2 = {1 : 'one', 2 : 'two' , 3 : 'three'}
print('Dictionary with integer keys ---> ' ,dict2)

### Creating an Empty dictionary and creating with interger keys
print('\n# # #Creating an Empty dictionary) and creating with interger keys ')

dict1 = {}
print('Empty ' ,dict1)

dict2 = {1 : 'one', 2 : 'two' , 3 : 'three'}
print('Dictionary with integer keys ---> ' ,dict2)

### Creating with mixed keys
print('\n# # #Creating with mixed keys ')

dict2 = { 'start' : 'one', 2 : 'two' , 3.3 : 'three' , 'tokens' : [10,20,30]}
print('Creating with mixed keys ---> ' ,dict2)

### Creating with dict() method
print('\n# # #Creating with dict() method ')

dict2 = dict({ 'start' : 'one', 2 : 'two' , 3.3 : 'three' , 'tokens' : [10,20,30]})
print('Creating with dict() method ---> ' ,dict2)

### Creating with each item as a pair
print('\n# # #Creating with each item as a pair ')

dict2 = dict([ ('start' , 'one'), (2 , 'two') , ('tokens' , [10,20,30])])
print('dict([ (\'start\' , \'one\'), (2 , \'two\') , (\'tokens\' , [10,20,30])]) ---> ' ,dict2)

### Creating a nested dictionary
print('\n# # #Creating a nested dictionary ')

dict2 = dict( {1: 'one' , 2 : 'two' , 3: { 31: 'three A', 32 : 'three B'}})
print('dict( {1: \'one\' , 2 : \'two\' , 3: { 31: \'three A\', 32 : \'three B\'}}) ---> ' ,dict2)


