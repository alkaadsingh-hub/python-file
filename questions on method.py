#create a student class that takes name and marks of 3 subjects as arguments in constructor.
#then create a method to print the average.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
       


    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name, "your average score is:" , sum/3)


#creating an object
s = Student("raghav", [30, 60, 50])
s.get_avg()































