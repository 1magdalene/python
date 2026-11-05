#Parent class/Super class/Base class
class Animal:
    isMammal = True
    age = 3

    def movement(self):
        print("Animal is moving")

#Child class/ Sub class/Derived class
class Dog(Animal):
    def bark(self):
        print("Woof! Woof! Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

dog1 = Dog()
dog1.movement()
print(dog1.isMammal)

cat1 = Cat()
cat1.movement()