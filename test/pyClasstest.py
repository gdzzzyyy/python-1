#def __init__(self, ...)
#def __del__(self,...)

class Test(object):
    pram1 = "abc"

    def __init__(self, name, age, city):
        self.name = name
        self._age = age
        self.__city = city
    
    def get_city(self):
        return self.__city

    @classmethod
    def get_pram (thisClass):
        return thisClass.pram1

    @property
    def setUI(self):
        return self.name


class JICHENG(Test):
    pass



if __name__ == '__main__':
    '''tx = Test('yao', 24, 'shanghai')
    print dir(tx)
    print tx.__dict__
    print tx.get_city()
    print tx._Test__city
    print Test.get_pram()
    print tx.setUI'''
    JC = JICHENG("zhu", 24, 'shanghai ')
    print dir(JC)