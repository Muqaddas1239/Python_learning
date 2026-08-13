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
