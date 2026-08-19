#1. Python Iterators:
# Iterator is an object that allows us to access the elements of a collection one at a time
numbers=[10, 20, 30, 40]      #created a list
my_iter=iter(numbers)       #created an iterator from list
print(next(my_iter))        #gets first item
print(next(my_iter))        #gets next

#Iterable: is an object that can be looped through one by one

numbers=[10, 20, 30, 40]
for i in numbers:
    print(i)

#Iterator with strings:

name="Python"
my_iter=iter(name)        #created an iterator
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#Stoplteration: occurs when there are no more items in an iterator
listn=[10, 20]
my_itern=iter(listn)
print(next(my_itern))
print(next(my_itern))
#print(next(my_itern))      #causes stoplteration
 
#2. Python Module: is a Python file that contains reuseable code, such as functions, variables, and classes
# modules are built in and also manually created

#Built-in Module: math 
#provides mathematical functions and operations

import math      
print(math.sqrt(25))     #calculates square root
print(math.pow(9,2))     #power function
print(math.ceil(2.2))    #rounds up
print(math.floor(4.8))   #fictorial

#Built-in Module: random
import random             #it provides functions for generating random values
number= random.randint(1,10)
print(number)

#Built-in datetime module: used to work with dates and times
import datetime
today= datetime.date.today()       #todays date from computer
print(today)
now=datetime.datetime.now()     #todays date and time
print(now)

#Buit-in json Module: used work 
#The json module is a built-in Python module used to work with JSON data.
#JSON stands for JavaScript Object Notation. 
# #It is commonly used to store and exchange data between applications, websites, and APIs.

#json.loads() → Converts JSON → Python

import json

data = '{"name": "Ali", "age": 22}'

person = json.loads(data)        #Converts a JSON string into a Python dictionary

print(person["name"])           #Gets the value of the "name" key

#json.dumps() → Converts Python → JSON

import json

person = {"name": "Ali", "age": 22}      

data = json.dumps(person)

print(data)

#Python RegEx module:(re)
#module is a built-in Python module used to search, match, and manipulate patterns in text.

#Regex is short for Regular Expression

import re

text = "My phone number is 0300-1234567"

result = re.search(r"\d+", text)    # re.search(): Searches the text for the pattern
#\d → matches a digit (0–9)     # + → matches one or more digits 
print(result.group())      

#re.findall(): Finds all matches

import re

text = "I have 2 apples and 5 oranges."

numbers = re.findall(r"\d+", text)

print(numbers)

#re.match(): Checks for a match at the beginning

import re

text = "Python is easy"

result = re.match("Python", text)

print(result.group())

#re.sub():Replaces matching text

import re

text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)
