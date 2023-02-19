import sympy

class Base:
    def __init__(self):
        self.formula = None

    def calc(self):
        self.formula = sympy.sympify('x**2+4*x+4')
        print(self.formula.factor())