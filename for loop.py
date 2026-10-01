# ## FOR LOOP:-
# #For loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. It allows you to execute a block of code multiple times for each item in the sequence.



# ##syntax of for loop:-

# # list/tuple/string = [52, 07,...........]
# #     for el in listname:
# #     print(el)

# # here el is element name which is given by the developer any name  can be given 
# # listname is the varaible that we are creating for tuple ,list,or string 

nums = [1, 2, 3, 4, 5, 6]

for value in nums:
    print(value)



tup = ("apple", "banana", "cherry")
for fruit in tup:
    print(fruit)




str = "alka singh"
for char in str:
    print(char)



##we useWHILE LOOP when we have to work with itertor means to work with variable when have tochange the variable or update the variable we use WHILW LOOP for that.
## We use FOR LOOP when we have to work with sequencial data or want to traverse on data   like list, tuple, string, dictionary, set etc.
##when we use FOR LOOP AND WHILE LOOP we have a option to use else statement with it. It is not mandatory to use.
 




#else :-
#this is optional . we use else statement with for loop and while loop when we want to execute a block of code after the loop has finished executing. 
##IT WORKS WHEN LOOP IS END.

veg = ["carrot", "potato", "tomato", "onion"]

for char in veg:
    print(char)
else:
    print("loop is finished")
























































































