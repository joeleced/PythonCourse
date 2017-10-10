n = int(input())
integer_list = list(int(x) for x in input().split())
for i in integer_list:
    tup = tuple(integer_list)
print(hash(tup))