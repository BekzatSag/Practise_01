a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())

a = " Hello, World! " #The strip() method removes any whitespace from the beginning or the end:
print(a.strip()) # returns "Hello, World!" 


a = "###Hello, World!###"
print(a.strip('#')) 

a = "Hello, World!"
print(a.replace("H", "J"))

#the split method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 


a = "apple,orange,banana,grape"
print(a.split(",", 2))  

