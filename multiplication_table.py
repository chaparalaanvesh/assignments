#multiplication table program using inheritance concepts


class multiplication():
    def __init__(self,number):
        self.number = number
    def result(self):
        a = []
        for i in range(0,11):
            a.append(self.number*i)
        return a



class table(multiplication):
    def __init__(self,number):
        multiplication.__init__(self,number)
        a1 = multiplication(number)

    def mul_table(self):
        b = self.result()
        for i in range(1,11):
            print self.number, 'x', i, '=', b[i]



a2 = table(2)
print a2.mul_table()







