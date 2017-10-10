numbers = [1,2,3]
formatStr = "Numbers are {0},{1},{2}".format(numbers[0],numbers[1],numbers[2])
print(formatStr)

formatStr = "{x}/{y}".format(x=100,y=1000)
print(formatStr)

joinStr = ' & '.join(["Apples","Oranges","Mangoes"])
print(joinStr)

originalStr = "Hello There"
replaceStr = originalStr.replace("There","World")
print(replaceStr)

str = "This is a monday"
print(str.startswith("This"))
print(str.endswith("day"))

print(str.upper())

print(str.lower())

print(min(1,2,3,5))
print(max(45,3,125))

print(abs(-125))