def mapDef(x):
    return x * x

map1 = map(mapDef, [2, 4, 6, 8, 10])
print(map1, type(map1))

def reduceDef(x, y):
    return x + y

reduce1 = reduce(reduceDef, [1, 2, 3, 4,5 ,6, 7])
print(reduce1)

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

map2 = map(char2num, '13579')
print(map2)