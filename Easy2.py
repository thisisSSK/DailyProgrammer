__author__ = 'thisisSSK'
"""
to create a calculator application that has use in your life.
It might be an interest calculator, or it might be something that you can use in the classroom.
For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions!
Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!
"""

class Calculator(object):
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.op = operation

    def displayEquation(self):
        print self.a, + self.operation, +self.b

    def calculate(self):
        if self.op.lower() == 'x' or self.op == '*':
            return self.a * self.b
        elif self.op == '/':
            return self.a / self.b
        elif self.op == '-':
            return self.a - self.b
        elif self.op == '+':
            return self.a + self.b
        else:
            return "Unsupported operation"

class TipCalculator(Calculator):
    def __init__(self, subTotal,tipPercent):
        Calculator.__init__(self, subTotal, float(tipPercent)/100 , '*')

newTip = TipCalculator(100,15)

