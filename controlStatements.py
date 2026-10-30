#Program to check if one is allowed to vote
age = 20

if age >= 18:
      print("You are old enough to vote")
else:
      print("You are cannot vote")

#Program to allow users input data
year = input("Enter your age: ") #Any value input through this is assumed to be a string
age = int(input("Enter your age: ")) #To convert the value to integer

if age >= 18:
      print("You are old enough to vote")
else:
      print("You are cannot vote")

#Typecasting - converting one data type to another
x = float(30) #convert value to decimal
y = int(4.15) #convert float valie to integer
print(x)
print(y)
