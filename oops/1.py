class Batch:
    batchno=22
    @classmethod
    def setbatchno(cls,new_batch):
        cls.batchno=new_batch
        print(cls.batchno,"Inside the cls method")
    def setdetails(self,name,course):
        self.name=name
        self.course=course
    def display(self):
        print("Welcome to {self.course} course {self.name} {Batch.batchno}")

    @staticmethod
    def fee():
        return '50k'
    

teja=Batch()
Dinesh=Batch()

teja.setdetails("Teja","python")
Dinesh.setdetails("Dinesh","Java")
teja.name="sai teja"
teja.display()
Dinesh.display()
print(Batch.batchno)
Batch.setbatchno(26)
print(Batch.fee)