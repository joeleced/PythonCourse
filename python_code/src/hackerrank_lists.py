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

options.
# print('--', options.keys())
# print('!!', options.values())

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