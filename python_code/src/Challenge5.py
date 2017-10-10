a = int(input())
b = int(input())

def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Error")

div(a,b)