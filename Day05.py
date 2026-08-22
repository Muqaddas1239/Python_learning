#Python Functions:
#1.Pass in functions: is a placeholder means do nothing for now

def fun():
    pass             #pass in function
fun()   #call the function

#pass in conditional statements
x=10
if x>5:      
    pass            # placeholder for future logic
else:
    print("x is 5 or less")

#pass in loops
for i in range(8):
    if i==2:
        pass            #do nothing when i is 2
    else:
        print(i)

#2.Global and Local Variables in python
#Local variables are defined inside the  function and exist only during its execusion, cannot be accessed from outside the function

def greet():
    msg="Hii MUQADAS"
    print(msg)         #local variable msg
greet()
#print(msg) will give error bcs we are calling it from outside the function

#Global variables are declared outside all functions and can be accessed anywhere in the program, including inside functions

show="Python is  good"
def display():
    print("Inside function:",show)
display()
print("Outside function:",show)

#Recursion in python: is a technique where a function to solve the problem step by step
#Syntax:
#def recursive_function(parameters):
 #   if base_case_condition:
 #       return base_result
  #  else:
   #     return recursive_function(modified_parameters)
def factorial(n):
    if n==0:         #Base case
        return 1
    else:         #recursive case
        return n* factorial(n-1)
print(factorial(8))

#Tail recursion: The recursive call is the last operation performed by the function
def count(n):
    if n==0:
        return
    print(n)
    count(n-1)   # last operation
    print(count(7))

#Non Tail recursion: The function has to do somthing after the recursive call returns
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(4))

#3. *args and **kwargs in Python
#These are used when you dont know beforehand how many arguuments will be passed to a function 
#*args allows a function to receive many positional arguments

def numbers(*args):
    print(args)
numbers(10, 20, 30)

#**Kwargs allows a function to receive many kayword arguments(arguments with names)

def student(**kwargs):       #many values with names
    print(kwargs)
student(name="FARHAN", age=22, subject="Math")

#4. First class functions in Python: functions as treated like values/ data

def msg(name):
    return f"Hi ,{name}"
f=msg     #assinging function to variable
print(f("Muuqadas"))

def argu():
    print("GOOD")
def call_function(func):     #passing a funtion as an argument
    func()
call_function(argu)

#4. Python Lambda Function: is a small, one line function without a name
square=lambda x:x*x    
print(square(7))          #syntax: lambda arguments: expression

#map(): applies same operation to every item in a list

Numbers=[1, 2, 3, 4]
result=map(lambda x: x*2, Numbers)
print(list(result))

#filter(): is used when we want to select only the items that satisfy a condition

nuum=[1, 2, 3, 4]
ans=filter(lambda x: x% 2==0,nuum)
print(list(ans))

#reduce(): it takes items and combines them step by step to produce one final result

from functools import reduce     #we need to import it
NUM=[1, 2, 3, 4, 8]
Result=reduce(lambda a, b:a+b, NUM)
print(Result)

