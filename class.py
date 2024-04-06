#!/usr/bin/python

class Calculator:
    def __init__(self,ina,inb):
        self.a = ina
        self.b = inb
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b

newCalculation = Calculator(10,20)

print newCalculation.add()

