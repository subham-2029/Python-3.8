#Comparison Operators in string

print("a"=="a")  # True, both are equal
print("a"=="b")  # False, both are not equal
print("a"!="b")  # True, both are not equal
print("a"!="a")  # False, both are equal
print("a"<"b")   # True, 'a' comes before 'b'
print("abc"=="abc") # True, both are equal
print("abc"<"abd") # True, 'abc' comes before 'abd'
print("abc"<"ab")  # False, 'abc' is longer than 'ab'
print("abc">"ab")  # True, 'abc' is longer than 'ab'
print("abc"<"abcd") # True, 'abc' comes before 'abcd'
print("abc">"abcd") # False, 'abc' comes before 'abcd'