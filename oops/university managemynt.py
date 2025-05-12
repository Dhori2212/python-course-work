from abc import ABC, abstractmethod

class person(ABC):
    def __init__(self, name, age):
        self.name=name
        self.age=age

    @abstractmethod
    def get_role(self):
        pass
    def get_basic_info(self):
        return f"Name:{self.name}, Age: {self.age}"
    def get_details(self):
        return f"{self.get_basic_info()}, Role: {self.get_role()}"
    

class student(person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name,age)
        self._student_id = student_id
        self._course = course
    def get_role(self):
        return "Student"
    def get_student_info(self):
        return f"{self.get_details()}, ID: {self._student_id}, Course: {self._course}"
    
class professor(person):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age)
        self._emp_id = emp_id
        self._department = department
    def get_role(self):
        return "Professor"
    def get_professor_info(self):
        return f"{self.get_details()}, Employee ID: {self._emp_id}, Department: {self._department}"
class AdminStaff (person):
    def __init__(self, name, age, staff_id, designation):
        super().__init__(name,age)
        self._staff_id = staff_id
        self._designation = designation
    def get_role(self):
        return "Admin Staff"
    def get_staff_info(self):
        return f"{self.get_details()}, staff ID: {self._staff_id}, Designation: {self._designation}"
    

class University:
    university_name = "parul university"
    def __init__(self):
        self.__people = []
    def add_person(self, person):
        self.__people.append(person)
    def display_all(self):
        for person in self.__people:
            print(person.get_details())

    @classmethod
    def get_university_name(cls):
        return cls.university_name
    @staticmethod
    def welcome_message():
        return f"welcome to parul university"
     
print(University.welcome_message())
print("university:", University.get_university_name())

u = University()
s1=student("Dinesh",22,106,"Python")
p1=professor("Teja",50,112,"cse")
a1=AdminStaff("Dhoni",45,108,"HOD")

u.add_person(s1)
u.add_person(p1)
u.add_person(a1)

print("\nAll Registered people:")
u.display_all()

print("\nDetailed Info:")
print(s1.get_student_info())
print(p1.get_professor_info())
print(a1.get_staff_info())







