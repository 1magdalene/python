
#Any name followed by a bracket is a function or a method
#While loop - has three steps; initialize, set the condition, increment/decrement
number = 15 #initialization

while number <= 25: #Condition
    print(number)
    number += 1  #Increment/Decrement

#For loop
for x in range(11): #It assumes it will start from 0
    print(x)

for y in range(20, 26): #means it'll start counting from 20 and the last value is 25
    print(y)

for z in range(10, 26, 2): #means that the values should increment by 2
    print(z)

for a in range(100, 91, -2): #to decrement by 2
    print(a)
