class EvenorOdd:
    def __init__(self,num):
        self.num=num
    def check(self):
        if self.num%2==0:
           return "Even Number"
        else:
            return "odd Number"
        

while True:
    n=int(input('Enter the number(0 Exit): '))
    if n!=0:
        ch=EvenorOdd(n)
        print(ch.check())
    else:
        break
     