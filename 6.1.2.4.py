import random
class Stack:    # defining the Stack class
    def __init__(self):    # defining the constructor function
        self.__stacklist = []
    def pop(self):
        val = self.__stacklist[-1]
        del self.__stacklist[-1]
        return val
    def push(self,object):
        self.__stacklist.append(object)
    def size(self):
        return len(self.__stacklist)
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def getSum(self):
        return self.__sum

stack1 = AddingStack()   # instantiating the object
for i in range(random.randrange(5,20)):
    var = random.randrange(1,10)
    stack1.push(var)
print("Sum is: ",stack1.getSum())
for i in range(stack1.size()):
    print(stack1.pop())
print(stack1.__dict__)