#Understanding integers and floats
a=25  #this is a normal number
b=13.2  #this is a number with decimal points 
print(type(a))
print(type(b))

#Understanding boolean and complex
c=True
d=5+6j
print(type(c))
print(type(d))

#Understanding Strings 
e='Python is fun'  #enclosed with single quotes
f="Python is easy"  #enclosed with double quotes
g='''Python is Interactive'''   #enclosed with triple quotes
# All Quotes are used to represent string data type
print(type(e))
print(type(f))
print(type(g))

#Understanding list, tuple and dictionary
h=[10,20,30,40]  #list is represented with square brackets
i=(10,20,30,40)  #tuple is represented with round brackets
j={1:'Python',2:'is',3:'fun'}  #dictionary is represented with curly brackets
print(type(h))  
print(type(i))
print(type(j))

#Understanding set and frozenset
k={10,20,30,40}  #set is represented with curly brackets
l=frozenset({10,20,30,40})  #frozenset is represented with frozenset() function
print(type(k))
print(type(l))
