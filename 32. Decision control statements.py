# Get user input for a number
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Illustrating if-elif-else statement
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")

# Illustrating a simple if statement
if number % 2 == 0:
    print(f"The number {number} is even.")

# Illustrating a nested if statement
if number >= 0:
    if number % 5 == 0:
        print(f"The non-negative number {number} is a multiple of 5.")
    else:
        print(f"The non-negative number {number} is not a multiple of 5.")
else:
    print(f"The number {number} is negative, so we cannot check if it's a multiple of 5 in this specific nested condition.")