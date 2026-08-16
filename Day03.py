#1.Python Loops:A loop allows us to execute the same  lock of code repeatedly
for i in range(4):      # syntax: for variable in sequence:
    print(i)          # for loop repeat something over a known range of values

name="Python"
for letter in name:         #loop for string
    print(letter)      

i=0
while i<7:         #while loop is used to keep repeating something as long as a condition is True
    print(i)        # syntax: while condition:
    i+=1

#2.Python Functions:
#A function is a reusable block of code that performs a specific task
#syntax:   def function_name(): 
def greet():
    print("Hi, its me.")
greet()     #calling function

# function with parameter: is a variable that receives a value when function is called
def greet_u(name):
    print("Hii",name)
greet_u("ALI")
greet_u("MUQADAS")

#function with default parameter
def welcome(name="student"):
    print("Welcome",name)
welcome()
welcome("MUQADAS")

def add(a,b):         #function with multiple parameters
    print(a+b)
add(10,20)
add(11,99)

#The return statement: return sends a value back from the function.
def add_numbers(a,b):
    return a + b
result=add_numbers(10,80)
print(result)

#3.range() function: used to genetate a sequence of numbers
#syntax: range(start, stop, step)
for i in range(2, 30, 3):
    print(i)
for i in range(8):    #range(stop)
    print(i)          
for i in range(2, 5):    #range(start, stop)
    print(i)

#4.Python Arrays:An array is a collection of multiple values (same data type) stored together
marks=[28, 82, 90]   #A list is a built in python data type
print(marks)

#NumPy is a library used for numerical computing
import numpy as np
numbers=np.array([10, 20, 30])
print(numbers)
numbers[1]=29      #changing element by index
print(numbers)

#Mathematical operations
numbers=np.array([10, 20, 30])
print(numbers * 2)
print(numbers + 3)
print(numbers - 4)
print(numbers / 2)

#Useful numpy functions
numbers=np.array([10, 20, 30])
print(numbers.sum())
print(numbers.mean())
print(numbers.max())
print(numbers.min())