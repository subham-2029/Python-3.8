# --- 1. For Loop ---
print("--- For Loop Examples ---")

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Iterating over a list:")
for fruit in fruits:
    print(f"  Current fruit: {fruit}")

# Iterating over a string
name = "Python"
print("\nIterating over a string:")
for char in name:
    print(f"  Current character: {char}")

# Iterating using range()
print("\nIterating using range():")
for i in range(5):  # Iterates from 0 to 4
    print(f"  Number: {i}")

print("\nIterating using range(start, end):")
for i in range(2, 7): # Iterates from 2 to 6
    print(f"  Number: {i}")

print("\nIterating using range(start, end, step):")
for i in range(1, 10, 2): # Iterates from 1 to 9, stepping by 2
    print(f"  Number: {i}")

# --- 2. While Loop ---
print("\n--- While Loop Examples ---")

# Basic while loop
count = 0
print("Basic while loop:")
while count < 3:
    print(f"  Count is: {count}")
    count += 1

# While loop with user input validation
print("\nWhile loop with user input validation:")
user_input = ""
while user_input.lower() != "exit":
    user_input = input("  Enter 'exit' to quit: ")
    if user_input.lower() != "exit":
        print(f"  You entered: {user_input}")

# --- 3. Loop Control Statements ---
print("\n--- Loop Control Statements ---")

# Break statement in for loop
print("\nBreak statement in for loop:")
numbers = [1, 2, 3, 4, 5, 6, 7]
for num in numbers:
    if num == 5:
        print("  Found 5, breaking the loop.")
        break
    print(f"  Processing number: {num}")

# Continue statement in for loop
print("\nContinue statement in for loop:")
for i in range(1, 6):
    if i % 2 == 0:  # Skip even numbers
        print(f"  Skipping even number: {i}")
        continue
    print(f"  Processing odd number: {i}")

# Break statement in while loop
print("\nBreak statement in while loop:")
j = 0
while True: # Infinite loop until break
    print(f"  Current value of j: {j}")
    if j >= 3:
        print("  j is 3 or more, breaking the loop.")
        break
    j += 1