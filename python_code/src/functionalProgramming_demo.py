##
def add_ten(x):
    return x+10

def twice(func,arg):
    return func(func(arg))

print(twice(add_ten,10))

## Lambdas
result = (lambda x : x**2)(30)
print(result)

print((lambda y : y**3)(5))

result = lambda x : x**3
print(result(5))

fun = lambda x,y : x+y
print(fun(1,2))
print((lambda x,y : x+y)(15,10))

## Map
def add(x):
    return (x+2)

nums = [10,20,30,40,50]
result = list(map(add,nums))
print(result)
result = list(map(lambda x:x+5,nums))
print(result)

## Filters
nums = [1,3,4,5,7,9,24,25,52]
result = list(filter(lambda x : x % 2 == 0, nums))
print(result)

def isOdd(x):
    if x % 2 != 0:
        return True

result = list(filter(isOdd, nums))
print(result)

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print (list(result))

result = filter(lambda x: x % 2 == 0, fib)
print (list(result))

## Generators
def function():
    counter = 0
    while counter < 5 :
        yield counter
        counter += 1

for x in function():
    print(x)

def evenNumbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(evenNumbers(11)))