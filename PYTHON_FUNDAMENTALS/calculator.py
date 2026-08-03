class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return a//b


print(calculator.add(5,10))
print(calculator.sub(5,10))
print(calculator.mul(5,10))
print(calculator.div(5,10))
