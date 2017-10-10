# p = input("Enter p value")
# n = input("Enter n value")
# r = input("Enter r value")
#
# p = int(p)
# n = int(n)
# r = int(r)
#
# si = (p * n * r) / 100
#
# print("Simple interest is - ", si)

# names = ['asd', 'asd', 'qwe', 'asd']
# if 'asd' in names:
#     names.append('test')
#     size = names.count('asd')
#     names.insert(1, 'dsa')
# print(names)
# print(size)
# print(len(names))
# print(names.index('test'))

# numbers = list(range(0, 101,5))
# print(numbers)

# def func():
#     print("Joel")
#     print("Johnson125")
#     print("Johnny")
#
# func()
# func()

# for i in range(1, 11):
#     print(i)
#
# fruits = ['apple','mango','grapes']
# for fruit in fruits:
#     print(fruit)
#
# evens = list(range(1,21))
# for num in evens:
#     if num%2 == 0:
#         print(num)

# counter = 0
# while counter <= 10:
#     print(counter)
#     counter += 1

# define the function blocks
def insertOp(i,elem):
    nums.insert(i,elem)

def printOp():
    print(nums)

def sortOp():
    nums.sort()

def popOp():
    nums.pop();

def removeOp(elem):
    nums.remove(elem)

def appendOp(elem):
    nums.append(elem)

def reverseOp():
    nums.reverse()

# map the inputs to the function blocks
options = {'insert' : insertOp,
           'print' : printOp,
           'sort' : sortOp,
           'pop' : popOp,
           'remove' : removeOp,
           'reverse' : reverseOp,
           'append' : appendOp
}

def process(s):
    command = s[0]
    commandLength = len(s)
    if commandLength == 3:
        options[command](int(s[1]),int(s[2]))
    elif commandLength == 2:
        options[command](int(s[1]))
    elif commandLength == 1:
        options[command]()

nums = []
n = int(input())
for i in range(n):
    s = input()
    s = s.split()
    process(s)





