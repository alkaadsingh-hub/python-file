str = 'this is first string'
str1 = "this is second string"
str2 = '''this is third string'''
print(str)
print(str1)
print(str2)


# #to print in new line we can use \n
var = "we are learning python. \nPython is mostly used in machine learning."
print(var)


# #tab space
var1 = "we are learning python. \tPython is mostly used in machine learning."
print(var1)



# ##BASIC OPERATIONON STRINGS
# ##1. concatenation  
a = "hello"
b = "world"
c = a + b
print(c)


string = "hello"
string1 = "python"
string2 = string + " " + string1  # we can use "" to add space between two strings
print(string2)


##2. length of string   
length = len(str)
print(length)


length1 = len(str1)
print(length1)


length2 = len(str2)
print(length2)





##INDEXING
a = "hello"
ch = str[2]
print(ch)  # it will print the character at index 2 which is 'l'


##in the form index we can only acess the  strings but cannot change it or manipulate it.


##SLICING 
#slicing means accessing the part of string.(can divide the string of can create a parts of a single string)
##most important part of python 


statement = "this is python program"
print(str[3:8])  #ending index is not included i.e. the output will be only "s is" not "s is p"


#to print the last string we add +1 in indexing or we use len(str) for example
statement = "this is python program"
print(statement[3:22])
     ##OR
print(statement[1:len(statement)])
     ##OR
print(statement[2:]) 


# # the above all syntax are correct 
print(statement[:8])  # python will automatically take "0" as starting index i.e. "0:8"


##NEGATIVE SLICING
#indexing start from negative 1


var = "apple" #indexing will  be apple = -5 -4 -3 -2 -1
print(var[-4:-2]) #ending indexnot included


##STRING FUNCTION
#1. str.endswith("er")
statement1 = "working on python code"
print(statement1.endswith("thon"))


statement2 = "working on python code"
print(statement2.endswith("ode"))


#2. str.capitalize function
var = "i am learning python"
print(var.capitalize()) #it work for only one time "print(var)" wil again print same statement in small character if we want  to print the statement in capital we need to store that variable
print(var)
#nowlets store it 
var = var.capitalize()
print(var)


#3. str.replace function()
var = "this is a python program"
print(var.replace("a", "o"))  #pass old value first then new one value 
print(var.replace("python", "java"))  #pass old value first then new one value


#4. str.find function()
str = "learning python from apna college"
print(str.find("i"))
print(str.find("from"))
print(str.find("z"))


#5. str.count function()
stat7 = "hello python"
print(stat7.count("o"))