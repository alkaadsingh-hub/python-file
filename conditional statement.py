#conditionalstatement
#1. if
#2. elif
#3. else



#1. if
#syntax
#if(condition):
#   print(statement)

age = 25
if(age >= 18):
     print("can vote")

#     #OR

age = 20
if(True):
    print("eligible")





#2. elif
#syntax
# elif(condition):
#   print(statement)


light = "yellow"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")

print("end of code")

#if condition statement is always get checked ..........while elif statement is only get checked when the if statement is not true. EXAMPLE is given below









#3.else
#else:
#    statement
subject = "maths"
if(subject == "english"):
    print("subject is english")
elif(subject == "computer science"):
    print("subject is CS")
elif(subject == "hindi"):
    print("subject is hindi")
else:
    print("subject not found")

print("end of subjects")

##else statement will print only when the above all condition get false i.e. if and elif satements get false






### NESTING

age = 5
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")    
else:
    print("cannot drive")




















































































































































































































































































































































