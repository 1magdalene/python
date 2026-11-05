# Object Oriented Programming
class Employee:
    # first member/property of a class are always variables which are the attributes

    def __init__(self, name, gender, position, age):
        self.name = name
        self.gender = gender
        self.position = position
        self.age = age

    # Functions - to show behavior
    def drive(self):
        print(f"{self.name} is driving...")

    def eat(self):
        print(f"{self.name} is eating...")

    def intro(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Position: {self.position}, Age: {self.age}")


class Manager(Employee):
    def __init__(self, name, gender, age, department, team_size):
        super().__init__(name, gender, "Manager", age)
        self.department = department
        self.team_size = team_size

    def lead(self):
        print(f"{self.name} is leading the {self.department} department with {self.team_size} team members.")


employee1 = Employee("Mark", "Male", "CEO", 67)  # Creating objects
print(employee1.name, employee1.gender, employee1.position, employee1.age)
employee1.drive()
employee1.intro()

employee2 = Employee("Jane", "Female", "Admin", 23)
employee2.drive()
employee2.eat()

employee3 = Employee("Joe", "Male", "HR", 45)
employee3.intro()

manager1 = Manager("Sarah", "Female", 38, "Operations", 12)
manager1.intro()
manager1.lead()

# Example of looping through objects
employees = [employee1, employee2, employee3, manager1]
for employee in employees:
    print(f"{employee.name} works as {employee.position}")