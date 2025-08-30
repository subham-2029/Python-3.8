# Undertsnading strings
# strings are text enclosed in single or double quotes
# also enclosed in triple quotes for multi-line strings

my_string = 'Hello, World!'
print(my_string)  # Output: Hello, World!
my_string2 = "Hello, World!"
print(my_string2)  # Output: Hello, World!
my_string3 = '''Hello,
World!'''   
print(my_string3)  # Output: Hello,
                   #         World!
print(type(my_string))  # Output: <class 'str'>
print(type(my_string2))  # Output: <class 'str'>
print(type(my_string3))  # Output: <class 'str'>

# Strings are immutable, meaning they cannot be changed after creation
# However, you can create new strings based on existing ones
new_string = my_string + " How are you?"
print(new_string)  # Output: Hello, World! How are you? 
print(my_string)  # Output: Hello, World!



