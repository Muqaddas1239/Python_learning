#1.Python Operators: operator is a symbol or keyword used to perform an operation on values or variables
# Arithmatic operators( +, -, *, /, %, //, **)
x=10
y=4
print(x+y)    #addition
print(x-y)    #subtraction
print(x*y)    #multiplication
print(x/y)    #division
print(x%y)    #modulus
print(x//y)   #floor division
print(x**y)   #power
#Assignment operator(=, cmpound assignment operators)
x=10
x+=5
print(x)
x-=3
print(x)
x*=2
print(x)
x/=4
print(x)
#Ternary operator: is a short way to write a simple if...else statement in one line
age=22
result="Adult" if age >=18 else "Minor"
print(result)
#Comparison operators: are used to compare two values
x=10
y=5
print(x==y)      #Equal to
print(x!=y)      #Not Equal to
print(x>y)       #Greater than
print(x<y)       #Less than
print(x>=y)      #Greater than equal to
print(x<=y)      #Less than or equal to
#Logical Operators: are used too combine multiple conditions (and, or, not)
age=22
has_id=True
print(age>=22 and has_id)      #both conditions must be true for and operator
has_permission=True
print(age>=18 or has_permission)         #at least one condition mmust be true
is_student=True
print(not is_student)           #reverses a boolean esult
# Identity Operators: used to check whether two variables refer to the same object in memory(is, is not)
w=[1, 2, 3]
v=w
print(w is v)    #check if two variables refer to the same object
r=[1, 2, 3]
s=[1, 2, 3]
print(r is not s)     #check if two variablesdo not refer to the same object

#Membership Operators: are used to check whether a value exists in a sequence such as string, list, tuple, or set

Fruits=["apple", "peach", "grapes"]
print("apple" in Fruits)        #Checks if a value exists
print("apple" not in Fruits)    #Checks if a value does not exist

#2. Built in data types :( List, Tuples, Set, Dictionary)
#List: are used to store multiple items in a single  variables i.e.,fruits

list=["abc", 34, True, 40, "male"]      #list with strings, integers and Boolean values

fruits = ["apple", "banana", "mango"]
print(fruits)                  # Creates and prints a list

fruits.append("orange")
print(fruits)                  # append() adds an item at the end

fruits.insert(1, "grapes")
print(fruits)                  # insert() adds an item at a specific index

fruits.remove("banana")
print(fruits)                  # remove() removes a specific item

fruits.pop()
print(fruits)                  # pop() removes the last item

print(len(fruits))             # len() returns the number of items

fruits[0] = "watermelon"
print(fruits)                  # Changes an item using its index

fruits.sort()
print(fruits)                  # sort() arranges items in ascending order

#Tuples:An ordered collection of items that cannot be changed after creation.

students = ("Ali", "Faizan", "Hamza")
print(students)         # Creates and prints a tuple

print(students[0])       # Access by index: Ali
print(len(students))       # len() returns number of students

#Sets:An unordered collection of unique items.

students = {"Ali", "Faizan", "Hamza"}
print(students)       # Creates and prints a set

students.add("Zain")       # add() adds a student at the end
print(students)

students.add("Ali")             # duplicate ignored
print(students)

students.remove("Ali")         # remove() removes a specific student
print(students)

print("Hamza" in students)        # Check if student exists: True
print(len(students))                # Number of students

#Dictionaries: A collection of key:value pairs.

students = {"1": "Ali", "2": "Faizan", "3": "Hamza"}
print(students)      # Creates and prints a dictionary

print(students["2"])        # Access by key: Faizan

students["4"] = "Zain"          # add() new student
print(students)

students["1"] = "Bilal"       # change value of key "1"
print(students)

students.pop("3")         # remove student with key "3"
print(students)

print(len(students))         # Number of students

#3.Condition (If, else, elif)
marks=75
if marks>=80:
    print("A Grade")           #checks the first condition
elif marks>=60:
    print("B Grade")        #checks another hcondition if if condition is false
else:
    print("C Grade")      #runs if all conditions are false
    