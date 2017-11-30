def testfilter(n):
    return n % 3 == 0

filterList = filter(testfilter, [1,2,3,4,5,6,7,8,9])
print(filterList)

def testFilterStr(n):
    return n != ''

filterListForStr = filter(testFilterStr, ['123', '','zhuyao','001',''])
print(filterListForStr)



'''filter的用法：
Python内建的filter()函数用于过滤序列。
    和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
