#File input/output:-
#python can be used toperform operations on file(read and write). 

#OPERATIONS ON FILES:-
#1. open a file
#2. read a file
#3. write a file



#1. open a file:-
#open() function is used to open a file in python. It takes two arguments: the file name and the mode in which the file is to be opened. The mode can be read, write, append, etc.

##syntax:-

# f = open("file-name", "mode")  #if we do not specify the mode, it will be opened in read mode by default. 

f = open("demo.txt", "r") #open the file in read mode

#right now wehave a file in vs code named demo.txt. butif we dont have a file inside the vs then we need to provide a path of the file to perform any operation on file 



#2. read a file:-
#now let perform some operations on the file.

# print(data)
# print(type(data)) #it will return the type of data which is string


#after performing the operations on file we need to close the file.
f.close() #it will close the file and free up the resources.


data = f.read(10) #it will read the first 10 characters of the file
print(data)


line1 = f.readline() #it will read the first line of the file
print(line1)







#writing a file:-
#before writing a file we need to open the file.

#syntax:-
# f = open("file_name ", "w")          #it will open the file in write mode. if the file does not exist, it will create a new file.
#f.write

f = open("demo.txt", "w") #open the file in write mode
f.write("python is most popular programming language") #it will overwrite the data (delete the first and thenadd new data)to the file.

f.close()


# if we do not want to overwrite the data in the file, we can use append mode.

f1 = open("demo.txt", "a") #open the file in append mode
f1.write("\npython is most popular programming language, it is easy to learn ") #it will add the data to the end of the file.
f1.close() #it will close the file and free up the resources.






#using r+ mode:-
f = open("sample file","r+")
f.write("no")
print(f.read())    #read the file to check the data in the file.



#using w+ mode:-
f = open("sample file", "w+")
print(f.read())       #it will return empty because it will overwrite the data in the file.



#Deleting a file :-
#to delete a file use module
#for now we are using "os" module which is pre installed.
#to use any module in python we need to import it by using key word as"import

#syntax:-
#import os
#os.remove(file_name)


import os

os.remove("sample file")






