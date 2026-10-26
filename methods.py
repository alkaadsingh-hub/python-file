#METHODS:-
#methods are functions that belongs to an object




# syntax for creating a method:-
# class classname:
#      def __init__(self,name,marks):
#       self.name = name 
#       self.marks = marks
#       
#      def method_name(self):
#           print("hellooo students")

#creating an object 
#s = Student("karan", 54)
#s.method_name()






 class Student:

     def __init__(self, name, contact):
         self.name = name
         self.contact = contact
     def hello(self):          #mehtod name
      print("hello students")





# #creating object 
# s = Student("karan", 513133563842)
# s.hello()





#we an access self properties
class College:
   name = "ABC college"    #class attribute

   def __init__(self, name, location):
      self.name = name     #object attribute
      self.location = location

   def university(self):
      print("welcome to college",self.name, self.location)


#creating an object
c = College("ABC college", "delhi")
c.university()








