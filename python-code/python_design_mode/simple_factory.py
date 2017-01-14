#!/usr/bin/env python2.7
# coding=utf-8

class Operation:
    def get_result(self):
        pass

class OperationAdd(Operation):
    def get_result(self):
        return self.op1 + self.op2

class OperationMul(Operation):
    def get_result(self):
        return self.op1 * self.op2

class OperationSub(Operation):
    def get_result(self):
        return self.op1 - self.op2

class OperationDiv(Operation):
    def get_result(self):
        try:
            result = self.op1 / self.op12
            return result
        except:
            print "div error."
            return 0

class OperationUndef(Operation):
    def get_result(self):
        print "undefine Operation"
        return 0

class OperationFactory:
    operation = {}
    operation["+"] = OperationAdd()
    operation["-"] = OperationSub()
    operation["*"] = OperationMul()
    operation["/"] = OperationDiv()

    def  createOperation(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op

if __name__ == "__main__":
    op = raw_input('operation:')
    opa = input("a:")
    opb = input("b:")
    factory = OperationFactory()
    cal = factory.createOperation(op)
    cal.op1 = opa
    cal.op2 = opb
    print cal.get_result()
