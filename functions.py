#Functions/methods - any line/block of code that performs a task within a program
#It's any name followed by a bracket
#print is also a method

#1. Standard Library Functions/Built-In Functions - Already exist
x = min(45, 89, 90, 32, 67, 57)
print(x)

y = max(45, 89, 90, 32, 67, 57)
print(y)

#2. User Defined Functions - Create and Define what it should do, should start with the key word def
def school():   #def + function name + brackets + :
    print("Emobilis")

#Calling the function
school()


def add():
    x = 10
    y = 20
    print(x + y)

add()

def addition(a, b): #Parameters = variables/values passed inside the brackets of a function
    print(a + b)

addition(10, 20) #A value is an argument only when its passed when calling the function