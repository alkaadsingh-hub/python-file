info = {
     "key" : "value", 
     "name" : "alka singh",
     "learning" : "python",
     "subjects" : ["maths", "c++", "python"],
     "marks" : ( 90, 80, 70, 60),
     "cgpa" : 8.25,
     "age" : 30,
     "pass" : True,
     }
print(info)
print(type(info))

# # In dictionary we can store different types of data like string, list, tuple, float, integer and boolean(only at value place).
# # in dictionary we can store data in key value pair. Key is unique and value can be duplicate.
# # in dictionary we cannot store list, and dictionary as key because they are mutable data types. We can store only immutable data types like string, integer, float and boolean as key. 




# # accessing the data from dictionary 
print(info["subjects"])
print(info["name"])

# #assining new value to existing key and adding new key value pair in dictionary

info["cgpa"] = 7.2 

info["surname"] = "singh" # adding new key value pair in dictionary

print(info)





# can create null dictionary
null_dict = {}
print(null_dict)
print(type(null_dict))

    




# #NESTED DICTIONARY
# # we can store dictionary inside dictionary. It is called nested dictionary.

student = {
    "student1" : "rahul kumar",
    "subject": {                      #nested dictionary
        "maths": 90,
        "english": 85,
        "science": 80,


    }
}
print(student)
print(student["subject"])
print(student["subject"]["maths"]) # accessing the value of nested dictionary






##Dictinary metheods
#1. myDict.keys() - returns all the keys of dictionary
#2. myDict.values() - returns all the values of dictionary
#3. myDict.items() - returns all the key value pairs of dictionary as tuple in list
#4. myDict.get(key) - returns the value of the specified key
#5. myDict.update(newDict) - updates the value of the specified key



#1. myDict.keys()
print(student.keys())
print(list(student.keys())) # converting the keys into list




#2. myDict.values()
print(student.values())
print(len(student))


#3. myDict.items()
print(student.items())




#4. myDict.get("key")
print(student.get("student1")) # returns the value of the specified key




#5. mDict.update(newdict)
student.update({"age": 25})# updates the value of the specified key
print(student)
























