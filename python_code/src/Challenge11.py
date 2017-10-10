prices = [50,100,1000,500]

result = list(map(int, map(lambda x : x - (x * 0.1), prices)))
print(result)