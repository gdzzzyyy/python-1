'''
学习Python的sort排序
    排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1，
这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序。
'''
def testSort(a, b):
    if a > b:
        return -1
    if a < b:
        return 1
    if a == b:
        return 0

testList = [4, 23, 66, 1, 11, 991]
sorted(testList, testSort)
print(sorted(testList, testSort))


print(sorted(testList))


'''
返回函数
    其实就是回调函数
    '''
def functionA(*agrs):
    def functionB():
        for k in agrs:
            print(k + '\n')
            return 0
    return functionB

functionA(1,2,3,4,5,6,7)