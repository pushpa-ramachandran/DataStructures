# ######################### Removing elements from the Set ##############################
# Use built-in remove() function but a KeyError arises if element doesn’t exist in the set.
# To remove elements from a set without KeyError, use discard(), if the element doesn’t exist in the set, it remains unchanged.
# Pop() function can also be used to remove and return an element from the set, but it removes only the last element of the set.
# If the set is unordered then there’s no such way to determine which element is popped by using the pop() function.
# To remove all the elements from the set, clear() function is used.


########### Removing elements from a set #########

### Removing an eleemnt - remove()
print('\n # # # Removing an eleemnt - remove() ')

list1 =[]
for i in range(1,10):
    list1.append(i*10)

set1 = set(list1)
print(set1)
set1.remove(10)
set1.remove(20)

print(' set1.remove(10) ;set1.remove(20) ---->' , set1)

### Removing an eleemnt - discard()
print('\n # # # Removing an eleemnt - discard() ')

print(set1)
set1.discard(10)
set1.discard(30)

print(' set1.discard(10); set1.discard(30) 10 already removed ---->' , set1)

### Removing an eleemnt - pop()
print('\n # # # Removing an eleemnt - pop() ')

print(set1)
set1.pop()

print(' set1.pop() ---->' ,'Element popped', set1.pop(),"After pop" , set1)
print(' set1.pop() ---->' ,'Element popped', set1.pop(),"After pop" , set1)

### Removing all eleemnts - clear()
print('\n # # # Removing all eleemnts - clear() ')

print(set1)
set1.clear()

print(' set1.clear() ---->' ,'Elements cleared---->', set1)
