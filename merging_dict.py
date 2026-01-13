d1 = {'a': 10, 'b': 20}
d2 = {'b': 30, 'c': 40}
result = d1.copy()
for i, j in d2.items():
    result[i] = result.get(i, 0) + j

print(result)
