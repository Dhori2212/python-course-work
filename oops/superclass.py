class parent:
    def __init__(self,fname):
        self.fname=fname
        print(f"Family first name added {self.fname}")

class Father(parent):
    def __init__(self,fname,flname):
        super().__init__(fname)
        self.flname=flname
        print(f"Father name added:{self.fname} {self.flname}")

class Mother(parent):
    def __init__(self,fname,mlname):
        super().__init__(fname)
        self.mlname=mlname
        print(f"Mother name added:{self.fname} {self.mlname}")

class child(Father):
    def __init__(self,fname,flname,cname):
        Father.__init__(self,fname,flname)
        self.cname=cname
        print(f"Child name added:{self.fname} {self.flname}  {self.cname}")

        
f=Father('ABC',"xyz")
m=Mother("ABC",'pqr')
c=child('ABC',"xyz",'mno')