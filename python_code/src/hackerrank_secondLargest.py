n = int(input())
arr = map(int, input().split())
largest = 0
second = 0
for x in arr:
    if x > largest:
        second = largest
        largest = x
    elif largest > x > second:
        second = x

print(second)