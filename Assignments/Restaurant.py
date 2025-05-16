from abc import ABC, abstractmethod

class person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass

    def get_basic_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    def get_details(self):
        return f"{self.get_basic_info()}, Role: {self.get_role()}"

# Subclasses for different roles
class Restaurant_Manager(person):
    def __init__(self, name, age, manager_id):
        super().__init__(name, age)
        self._manager_id = manager_id

    def get_role(self):
        return "Restaurant_Manager"

    def get_info(self):
        return f"{self.get_details()}, Manager ID: {self._manager_id}"

class Executive_Chef(person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self._emp_id = emp_id

    def get_role(self):
        return "Executive_Chef"

    def get_info(self):
        return f"{self.get_details()}, Employee ID: {self._emp_id}"

class server(person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self._staff_id = staff_id

    def get_role(self):
        return "Server"

    def get_info(self):
        return f"{self.get_details()}, Staff ID: {self._staff_id}"

class Busser(person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self._staff_id = staff_id

    def get_role(self):
        return "Busser"

    def get_info(self):
        return f"{self.get_details()}, Staff ID: {self._staff_id}"

class Food_runner(person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self._staff_id = staff_id

    def get_role(self):
        return "Food_runner"

    def get_info(self):
        return f"{self.get_details()}, Staff ID: {self._staff_id}"

class Cashier(person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self._staff_id = staff_id

    def get_role(self):
        return "Cashier"

    def get_info(self):
        return f"{self.get_details()}, Staff ID: {self._staff_id}"

class Dishwasher(person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self._staff_id = staff_id

    def get_role(self):
        return "Dishwasher"

    def get_info(self):
        return f"{self.get_details()}, Staff ID: {self._staff_id}"

# Restaurant Class
class Restaurant:
    Restaurant_name = "Pista House"

    def __init__(self):
        self.__people = []

    def add_person(self, person):
        self.__people.append(person)

    def display_all(self):
        for person in self.__people:
            print(person.get_details())

    def display_detailed_info(self):
        for person in self.__people:
            if hasattr(person, 'get_info'):
                print(person.get_info())

    @classmethod
    def get_Restaurant_name(cls):
        return cls.Restaurant_name

    @staticmethod
    def welcome_message():
        return "Welcome to Pista House"

# Main Program with Option Selection
def main():
    r = Restaurant()
    print(Restaurant.welcome_message())
    print("Restaurant:", Restaurant.get_Restaurant_name())

    
    people = [
        Restaurant_Manager("Dinesh", 22, 106),
        Executive_Chef("Teja", 50, 112),
        Cashier("Prudhvi", 32, 103),
        server("Dhoni", 45, 121),
        server("Bhavani", 34, 122),
        server("Ram", 35, 123),
        server("Ambi", 35, 124),
        Busser("Kalyani", 34, 106),
        Busser("Tharun", 24, 107),
        Busser("Prem", 30, 108),
        Busser("Ramya", 34, 109),
        Food_runner("Kuldeep", 32, 110),
        Food_runner("Kavitha", 38, 120),
        Food_runner("Kallu", 31, 130),
        Food_runner("Vinay", 30, 123),
        Dishwasher("Likitha", 34, 135),
        Dishwasher("Lalitha", 32, 136),
        Dishwasher("Lavanya", 33, 137),
        Dishwasher("Lalith", 35, 138),
        Dishwasher("Latha", 30, 139)
    ]

    for p in people:
        r.add_person(p)

    while True:
        print("\nChoose an option:")
        print("1. Display all registered people")
        print("2. Display detailed information")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print("\nAll Registered People:")
            r.display_all()
        elif choice == '2':
            print("\nDetailed Information:")
            r.display_detailed_info()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
