# Nested loops, break, continue, and pass statements in Python

# 1. Nested for loops
print("Nested for loops:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print()

# 2. Nested while loops
print("Nested while loops:")
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
print()

# 3. Using break in a loop
print("Using break in a for loop:")
for i in range(5):
    if i == 3:
        print("Break at i=3")
        break
    print(f"i={i}")
print()

# 4. Using continue in a loop
print("Using continue in a for loop:")
for i in range(5):
    if i % 2 == 0:
        print(f"Continue at i={i}")
        continue
    print(f"i={i}")
print()

# 5. Using pass in a loop
print("Using pass in a for loop:")
for i in range(3):
    if i == 1:
        pass  # Placeholder, does nothing
        print(f"Pass executed at i={i}")
    else:
        print(f"i={i}")
print()

# 6. Nested loops with break and continue
print("Nested loops with break and continue:")
for i in range(3):
    for j in range(3):
        if j == 1:
            print(f"Continue inner loop at j={j}")
            continue
        if i == 2 and j == 2:
            print("Break outer loop at i=2, j=2")
            break
        print(f"i={i}, j={j}")
    else:
        # This else executes if the inner loop wasn't broken
        print(f"Inner loop completed for i={i}")
print("Program finished.")