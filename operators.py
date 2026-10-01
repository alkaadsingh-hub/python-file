#operators perform operation on operands

#arithmetic operators
a = 10
b = 30

print(a + b)   #addition
print(a - b)   #subtraction
print(a * b)   #multiplication
print(a / b)   #division
print(a % b)   #modulus
print(a **b)   #exponentiation   The ** operator is used to raise a number to the power of another number.
print(a // b)  #floor division  It divides one number by another and rounds the result down to the nearest whole number (toward negative infinity).


 #relational operators
print(a == b) 
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a != b)


#assingment operators

num = 20
num = num + 5
print(num)
num += 10
print("num:" , num)

num1 = 10
num1 -= 3

num2 = 30
num2 *= 3

num3 = 15
num3 /= 3

num4 = 10
num4 %= 3

num5= 5
num5 **= 3

print("num1:", num1)
print("num2:", num2)
print("num3:", num3)
print("num4:", num4)
print("num5:", num5)    #power


#LOGICAL OPERATORS (AND, OR, NOT) ..........Works with boolean values (True or False) and are used to combine conditional statements.
##and operator (and) returns True if both statements are true
a1 = 10 
b1 = 20
print("and operator:", a1 > b1 and b1 > a1)

#not operator (not) returns True if the statement is false
print("not operator:", not(a1 < b1))

#or operator (or) returns True if one of the statements is true
print("or operator:", a1 < b1 or b1 < a1)