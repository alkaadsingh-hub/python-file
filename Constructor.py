#CONSTRUCTOR OR __init__("self") function :-
#Pyhton automatically call init() function eigther programmer call it or not but it is always excuted.
# all "classes" have a function called "__init__() function", which is always executed when the "object" is being initiated.

#If we want to write a constructor here is syntax:-

# #creating a class
# class House:
#     flatno = 105 
#     state = "delhi"
#     # def __init__(self):
#     #     print("we have created a constructor or init function")


# #creating an object 
# h1 = House()   #these parenthesis call init() function




# #now let's print "self"
# # class Home:

#     # state = "Himachal pradesh"
#     # def __init__(self):
#     #     print("we have created a constructor or init function")
#         # print(self)   #it will print the class name and object. Basically self == h2

# #creating an object 
# # h2 = Home()



# #we can pass multiple parameters in constructors .....self would always be first parameter.

# class School:
#     uniform = "blue and white"
#     school_name = "KSK academy"
#     def __init__(self, fullname, marks, rollno):   #The self parameter is a reference to the current instance of the class and isused to access variable that belongs tothe class.      "self" is an on oject and reference....., it can be named as an variable too(a, b, c, etc)....programmer uses "self" so that it does not create a confusion
#         self.name = fullname 
#         self.marks = marks
#         self.rollno = rollno      
#         print("fullname added")
#         print(self)


# #creating an object 
# s = School("Rahul singh",93, 5)  #rahul singh
# s1 = School("karan", 63, 6)


# print(s.name, s.marks, s.rollno)
# print(s1.name, s1.marks, s1.rollno)

# print(s.uniform) 
# print(s.school_name)
# The data that is stored inside the class, object or variable is called as "attributes".





#  def __init__(self, fullname):    # here "fullname" is parameter
#     self.name = fullname          # here "sellf.name" is.... which is going to create in a new object 













#can divide constructorin two parts 

class Flatno:
    #1. Default constructor
    def __init__(self):
        pass

    #2. Parameterized constructor(refers to the constructor where other parameter is also passed other than self)
    def __init__(self, address, floor ):
        self.address = address
        self.floor = floor
#creating an object 

flat = Flatno(860, "second floor")
print(flat.address, flat.floor)



