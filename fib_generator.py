class Fib:
    def __init__(self,nn):
        self.__m = 0
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        retur = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, retur
        return retur
class Class:
    def__init
for i in Fib(10):
    print(i)
