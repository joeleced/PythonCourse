# def add(a,b):
#     return a+b
#
# def square(a):
#     return a*a
#
#
# result = square(add(2, 3))
# print(result)

# try:
#     print(100/0)
# except ZeroDivisionError:
#     print('Error occured')
# finally:
#     print('Bye bye')

file = open('jfile.txt','a')
file.write("\nFifth Line")
file.close()

file = open('jfile.txt', 'r+')
file.write('Ayo poche')
print(file.read())
# line1 = file.readline()
# print(line1, end='')
# line2 = file.readline()
# print(line2, end='')
file.close()
