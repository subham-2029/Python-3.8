#Evaluation Of arithmetic operations
#expressions with single operator 
print(3+2)  #Addition
print(3-2)  #Subtraction
print(3*2)  #Multiplication
print(3/2)  #Division   
print(3//2) #Floor Division 

# Expressions with multiple operators are evaluated on the basis of operator precedence
print(3+2*5)  #Multiplication has higher precedence than addition
print((3+2)*5) #Parentheses have highest precedence
print(3+2**3)  #Exponentiation has higher precedence than addition
print(3**2*4) #Exponentiation has higher precedence than multiplication
print(3**2**3) #Exponentiation is right associative
print(3*4/2) #Multiplication and Division have same precedence and are evaluated from left to right
print(3*4//2) #Multiplication and Floor Division have same precedence and are evaluated from left to right
print(3*4/2**2) #Exponentiation has higher precedence than Multiplication