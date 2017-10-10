## Set
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)
print(5 in numbers)
numbers.add(25)
print('Add - ', numbers)
numbers.remove(6)
print('Remove - ', numbers)

set = {1,2,3,3}
print('Set # Duplicates removed - ', set)

seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}
print('Union - ', seta | setb)
print('Intersection - ', seta & setb)
print('Difference - ', seta & setb)

