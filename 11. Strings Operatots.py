# item assignemnt in strings is not supported
a = "hello"
a[0] = "H"
print(a) # TypeError: 'str' object does not support item assignment

# Traversing A sting
my_string = "Hello, World!"
for char in my_string:
    print(char)

#accessing characters in a string
print(my_string[0])  # H
print(my_string[-1]) # !
print(my_string[7])  # W

#string operators
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Hello World [Concatenation]
print(str1 * 3)          # HelloHelloHello [replication]


# String slicing
print(my_string[0:5])  # Hello  
print(my_string[:5])   # Hello
print(my_string[7:])   # World!

#Membership operators
print('H' in my_string)    # True
print('h' not in my_string) # True



