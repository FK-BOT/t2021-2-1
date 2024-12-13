#calculator problem-1
class Calculator:
    def __init__(self,a,b,operator):
        self.a=a
        self.b=b
        self.operator=operator
    def cal(self):
        if self.operator=='addition' or self.operator=='+':
            return self.a+self.b
        elif self.operator=='subtraction' or self.operator=='-':
            return self.a-self.b
        elif self.operator=='multiplication' or self.operator=='*':
            return self.a * self.b
        elif self.operator=='division' or self.operator=='/':
            if self.b==0.0:
                 return "divide by zero error"
            else:
                return self.a/self.b
        else:
            return "input a proper operator"
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
operator=input("enter operator:")
c=Calculator(a,b,operator)
res=c.cal()
print("result=",res)
