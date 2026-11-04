#Object Oriented Programming
class Employee:
    #First member/property of a class are always variables which are the attributes
    name = "John"
    gender = "Male"
    position = "Managing Director"
    age = 51

    #Functions - to show behavior
    def drive(self):
        print("Employee is driving...")

    def eat(self):
        print("Employee is eating...")

employee1 = Employee() #Creating objects
employee2 = Employee()
employee3 = Employee()