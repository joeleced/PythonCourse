## Dictionary Functions
people = {"John" : 30,"Jannet" : 26,5 : 'asd'}
print(people["John"])
people['Viji'] = 68
print(5 in people)

print(people)
print(str(people))
print(type(people))
del people[5]
print(people.get(5,None))

## Tuple
fruits = ('Apple','Mango') # Brackets are optional
# fruits[0] = 'Grapes'
print(fruits)
print(fruits[1:])
print(fruits[:1])

## List Slicing
names = ['joel', 'johnson', 'johnny', 'vj', 'ld', 'jj']
print(names[2:6])
print(names[:3])
print(names[3:])
print(names[1:6:2])

## List Comprehension
list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list)


