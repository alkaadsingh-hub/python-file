name = input("enter your name:")
print("welcome", name)


##input() results in string data type, even if you enter a number.

age = input("your age is:")
print(type(age))  #it will show string data type

##input() results in string data type, even if you enter a number. If you want to use the input as an integer or float, you need to convert it using int() or float() functions.

value = float(input("your product price is:"))
print("the final price is:", value)
print(type(value))


##programm
name = input("enter your name :")
rollno = input("enter your roll no. :")
marks = input("your makrs is:")

print("welcome", name)
print("rollno.:", rollno)
print("marks:", marks)






