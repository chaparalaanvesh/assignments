class Operator():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

class Result(Operator):
    def __init__(self,a,b):
        Operator.__init__(self,a,b)



result = Result(10,20)
print result.add()
print result.mul()
print result.sub()
print result.a
print result.b
