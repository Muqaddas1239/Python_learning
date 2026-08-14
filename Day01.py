#1:python syntax and identation
#syntax means rules for writing python code

print("This is Muqaddas Ameen")

#identation means spaces at the begininng of a line 
#identation define a block of code ,usually 4 spaces for identation

if 4>1:
    print("four is greater than one" )

#2:Variables in python
#used to store data, variable names are casse sensitive
#variable names not be any of the python keyword,not start with number, easy to understand

student_name="Muqaddas"
x=3
y=7
print(x)
print(y)

#multiple variables:
X,Y,Z="Apple", "Orange", "Cherry"
print(X)
print(Y)
print(Z)
#Print() function used to output , for multiple variables e.g:
print(X, Y, Z)
# we can also use + operator
print(X + Y + Z)

#Data types like int, float, string etc we use type function to check type of variable
print(type(student_name))
print(type(x))
print(type(X))

#3: Python String: is simply text written inside quotes either single or double quotes , string can contain letters, numbers, spaces, special characters.
name="MUQADAS"
age="23"
print(age)
print(type(age))      #to check type of a string
word="Python"         #indexing will be start through 0, not 1
print(word[3])
print(word[-1])        #start from end with index -1
print(len(word))       #len() function tells the number of characters in string (spaces also counted)
print(word[0:3])    #slicing: taking some part of string , syntax: string[start:end]
first_name="FAIZAN"
last_name="ALI"
full_name=first_name+" "+ last_name     #Cancatenation of string through + operator
print(full_name) 
value="Hi"
print(value * 3)    # sterik is used to repeat string
Name="ali"
print(Name.upper())      #upper() used to convert letters to uper case, similarly lower() for lower case
greet="  HELLO!  "
print(greet.strip())    # strip() removes extra spaces in beginning and ending
message="I like icecream"                                
sentence=message.split()     #split() divides string into a list
print(sentence)
print(greet.find("O"))   # find() tells us index position 
print(greet.count("L"))  # count()tells how many times something appears
print(f"My name is {name} and I am {age} years old.")       #f string used for putting variables inside string
print("Hello\nWorld")    #escape character \n new line
                        