class Calculator:
    def __init__(self,a,b,task):
        self.a=float(a)
        self.b=float(b)
        self.task=task
    def Calculate(self):
        if self.task=='addition':
            return self.a+self.b
        elif self.task=='substaction':
            return self.a-self.b
        elif self.task=='multiplication':
            return self.a*self.b
        elif self.task=='division':
            if self.b>0:
                return self.a/self.b
            else:
                return "error accured"
        else:
            return "invalid operation"
x=input("enter the value:")
y=input("enter the value:")
op=input("enter the operation:")
c=Calculator(x,y,op)
print("result:",c.Calculate())



