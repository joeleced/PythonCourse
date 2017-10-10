##Itertools
from itertools import count,accumulate,takewhile

## count function
for i in count(3):
    print(i)
    if i >= 20:
        break

## accumulate function
nums = [1,2,3,4,5]
print(nums)
print(list(accumulate(nums)))

print(list(accumulate(range(8))))

#takewhile function
nums = [1,2,3,4,5,6,7,8,9]
print(list(takewhile(lambda x : x <=5, nums)))

print(list(takewhile(lambda x : x < 10, list(accumulate(range(8))))))
