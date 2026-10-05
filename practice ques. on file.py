#question1.
#create a file "practice.txt" and add the following data in it:-
# hii everyone 
# # we are learning file i/o 
# # using python 
# # i like programming in java


open("practice.txt", "r")

with open("practice.txt", "w")as g:
    g.write("hii everyone \nwe are learning file i/o \nusing python \ni like programming in python")




#question2.
#WAP to replace the word "python" with "java" in the file "practice.txt".

with open("practice.txt", "r")as h:
   data = h.read()           #file is stored in data variable and we can perform operations on it.


new_data = data.replace("python", "java")  #it will replace the word python with java in the data variable.

with open("practice.txt", "w")as h:
    h.write(new_data)

print(new_data)







