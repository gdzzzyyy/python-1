'''list = [1,4, 111]
def showNum(*numList):
    print(len(numList))
    for num in numList:
        print(num)
    
showNum(list)

def makeUpTremp(name, age, **kw):
    print('name = ', name , ' age = ', age ,  ' ke = ', kw)
    #for n in kw :
     #   print(n)

trup = {"hell":"world", "shanghai":"city"}
makeUpTremp("join", "22", **trup)
'''
list2 = ['beijing','shanghai','guangzhou','shenzheng','nanjing']
r = []
def shuchu(n):
    for i in range(n):
        #print(list2[i])
        r.append(list2[i])
    #print(r)

shuchu(3)

#print(list2[-1:])
'''
list3 = list2[1:3]
print(list3)'''

def getList(*new):
    for n in new:
        print(n)
    

getList(*list2)