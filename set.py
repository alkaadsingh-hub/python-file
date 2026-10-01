#set
#set is unordered pair with unique identity
##  Set is MUTABLE but the element of set are IMMUTABLE 


A = {1, 2, 3, 4}
print(A)
print(type(A))


# Duplicate value are ignored in set

B = {"a", 2, 2, "b", "a", 3, 4, 5}

print(B)


#can print length of set

print(len(B))  #will print the total number of item.


#empty or nullset 

c = set()  #empty set; syntax
print(c)
print(type(c))




# Methods of set 

#1. add method
A.add(5)
A.add("alka")
print(A)



#2. remove method
A.remove(5)
print(A)




#3. clear method 
#used to make a set null

B.clear()
print(B)
print(len(B))






#4. pop method 
#removes a random value

print(A.pop())

print(A.pop())



#5. union method
#provde te sum of two set 

set = {1,2,5}
set1 = {4,2,3}

print(set.union(set1))




#6.intersection method
#provide common values 

setA = {"radha", "shyam", 7, 9, 10}
setB = {"ram", "raghav", "radha", 9, 10}

print(setA.intersection(setB))





































