print("Hello World!!")

#Strings
message = 'Hello world'
anotherMessage = 'this is a string'
doubleMessage = "This is also a string"
anotherString = "tests's tesing string"
multilineString = """This is a
multiLineString"""
print(message)
print(multilineString)

print(message[0])
print(message[-1])
print(len(message))


#Numerics
num = 5
numtype = type(num)
num1= 5.5
num1Type = type(num1)
print(num1)
print(num1Type)

#Variables
#variables start with underscores or letters
my_variable = "this is a valid variable name"


#Operators On Numeric data
#Addition +
#Subtraction -
#Multiplication *
#Division /
#Modulus %
#Exponent **
x = 10
y = 2
print(x+y) 
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

#Operators On String data 

string1 = "hello"
string2 = "world"
print(string1+ " " +string2) 

#Control Statements(Decisions)

num = 10
if num > 0:
    print("This number is greater than 0")
elif num == 0 :
    print("this number is 0")
else: 
    print("This number is less than 0")