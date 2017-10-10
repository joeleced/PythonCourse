class MyNumberOperator:

    def __init__(self,number):
        self.number = number

    def __mul__(self, other):
        return self.number + other.number


myop1 = MyNumberOperator(4)
myop2 = MyNumberOperator(3)
print(myop1 * myop2)
