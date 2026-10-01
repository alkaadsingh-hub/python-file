# #question1.

# #store the following word meaning in puthon dictionary  .......  cat : a small animal and table  "a piece of furniture", "list of facts and figure
# #solution

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts and figure"]

}

print(dictionary)








#question2.

#you are given a list of subject for students . assume one classroomis required for 1 subject . how many classes are needed by all the students.
#solution

subjects = {"python", "java", "c++", "python", "js", "java", "python", "java", "c++", "c"}

print(len(subjects))







# #question 3.

# #WAP to enter marks of 3 subject from the user and store themin a dictionary. start wiht an empty dictionary and add one by one .use subject name as key and amrks as value .
# #solution


marks = {}

x  = int(input("enter maths:"))
marks.update({"maths": x})

x  = int(input("enter chemistry:"))
marks.update({"chemistry": x})

x  = int(input("enter english:"))
marks.update({"english": x})


print(marks)







#quetion 4.
#find a way to store 9 and 9.0 as seperate value in set (can take helpof built in data type).


#without using built in data type we can strore same value in set with the help of string 

set = {9, "9.0"}

print(set)



#uing built in data type 

value = {
    ("float", 9.0),
    ("int", 9)
}

print(value)


