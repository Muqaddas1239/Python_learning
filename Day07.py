# Python OOP Concepts:
#Object Oriented Programming is a way of organizing code that uses objects and classes to represent real-world entities and their behavior

#1. Class: collection of objects , blueprints for creating objects
# A class defines a set of attributes and methods that the created objects (instances) can have

#2. Objects
#An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data

class Student:   #creating class with keyword class
        def study(self):             #Refers to the current object
                print("Student is studying")

#Creating an object of the Student class
student1=Student()         
student1.study()   #using object method


#3.Initiate Object with __init__()
# This method acts as a constructor and is automatically executed when an object is created

#Class of dog
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):    #automatically executed 
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.species)

#4.__str__() Method
#__str__() method allows us to define a custom string representation of an object

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)

#5. Constructors in Python
#Constructors are special methods used to initialize objects when they are created from a class

#__new__() Method: 
#This method is responsible for creating a new instance of a class. It allocates memory and returns the new object. It is called before __init__

class ClassName:
    def __new__(cls, parameters):
        instance = super(ClassName, cls).__new__(cls)
        return instance

#__init__() Method:
#This method initializes the newly created instance and is commonly used as a constructor in Python

class ClassName:
    def __init__(self, parameters):
        self.attribute = value

#5.1:Default Constructor: does not take any parameters other than self. It initializes the object with default attribute values

class Car:
    def __init__(self):

        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

car = Car()
print(car.make)
print(car.model)
print(car.year)

#5.2:Parameterized Constructor: accepts arguments to initialize the object's attributes with specific values

class Car:
    def __init__(self, make, model, year):   #self is a default argument
        self.make = make
        self.model = model
        self.year = year

car = Car("Honda", "Civic", 2022)
print(car.make)
print(car.model)
print(car.year)

