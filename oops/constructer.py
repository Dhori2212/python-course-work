class Batch:
 def __init__(self,username,password): 
     self.username=username
     self.password=password
 def login(self):
    if self.username and self.password:
       print("Login sucessfull",self.username)
    else:
       print("Enter the password or username correctly",self.username)



dinesh=Batch("Dinesh","Dinesh@123")

teja=Batch("Teja","")

dinesh.login()
teja.login()
    
    