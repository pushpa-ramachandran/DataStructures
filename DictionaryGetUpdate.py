########### Adding elements to a Dictionary #########
# Dict[Key] = ‘Value’.
# Updating an existing value in a Dictionary can be done by using the built-in update() method.
# Nested key values can also be added to an existing Dictionary.
# While adding a value, if the key value already exists,
# the value gets updated otherwise a new Key with the value is added to the Dictionary.

### Adding an eleemnt - Dict[Key] = ‘Value’
print('\n # # # Adding an eleemnt - Dict[Key] = ‘Value’ ')

dict1 = {}
dict1 [0] = "zero"
dict1 [1] = "one"

print(' dict1 = {} dict1 [0] = "zero") ---->' , dict1)

## Adding an eleemnt - update()
print('\n # # # Adding an eleemnt - update(dict1) ')

dict1 = {0: 'zero', 1: 'one'}
dict2 ={ 1: 'ones'}
dict1.update(dict2)

print('dict1.update(dict2)) ---->' , dict1)

## Adding an eleemnt - update()
print('\n # # # Adding an eleemnt - update({key : value}) ')

dict1 = {0: 'zero', 1: 'one'}
dict1.update({1:'oness' , 4: 'four'})

print('dict1.update({1:\'oness\' , 4: \'four\'}) ---->' , dict1)

## Accessing an eleemnt - using key
print('\n # # # Accessing an eleemnt - using key ')

dict1 = {0: 'zero', 1: 'one'}
dict1.update({1:'oness' , 4: 'four'})

print('dict1[1] ---->' , dict1[1])

## Accessing an eleemnt - using get()
print('\n # # # Accessing an eleemnt - using get() ')

dict1 = {0: 'zero', 1: 'one'}
dict1.update({1:'oness' , 4: 'four'})

print('dict1.get(4)' , dict1.get(4))
