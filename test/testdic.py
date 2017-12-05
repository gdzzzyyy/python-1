dic1 = {'name': 'zhuyao', 'age': '24', 'city':'xuancheng'}
'''
print(dic1)
for n in dic1:
    print(n)
    

for dicItem in dic1.itervalues():
    print(dicItem)

print('-----------------------')

for k, v in dic1.iteritems():
    print(k,'---',v)
    for n in v:
        print('value  str = ', n)



def deidai(index):
    list1 = [x * x for x in range(index, 5)]
    print(list1)


def deidai2():
    list2 = [x * x for x in range(1, 10)
        if x % 2 == 0]
    print(list2)

deidai2()

import os

list2 = [d for d in os.listdir('.')]
print(list2)
print('-----------1----------')

list2 = [k.lower() + ' + ' + v.upper() for k, v in dic1.iteritems()]
print(list2)

print('-----------2----------')

print(isinstance(list2, list), '        ', type(list2))


print('-----------3----------')


gener = (k.upper() + ' = ' + v.lower() for k, v in dic1.iteritems())
#print(gener.next())

print('-----------4----------')

def generar():
    for k in gener:
        print(k, "......gengerar")

generar()

print('------------5---------------')

def yieldReturn():
    print("step 1")
    yield 1
    print('step 2')
    yield 5
    print('step 3')
    yield 10

continueYiled = yieldReturn()
print(continueYiled.next())
print(continueYiled.next())
print(continueYiled.next())

'''

a_set = {1,2,3,4,5}
#print(a_set)

a_set.update([1,2,5,6,7,8])
print(a_set)
a_set.clear()
print(a_set)