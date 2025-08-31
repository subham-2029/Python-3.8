# Simple if statement
print("--- Simple if statement ---")
number = 10
if number > 5:
    print(f"{number} is greater than 5.")
# This block executes only if the condition (number > 5) is True.

print("\n--- if-else statement ---")
temperature = 25
if temperature > 30:
    print("It's a hot day!")
else:
    print("It's not excessively hot today.")
# The 'else' block executes if the 'if' condition is False.

print("\n--- if-elif-else statement ---")
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Below C")
# 'elif' (else if) allows checking multiple conditions sequentially.
# The first True condition's block executes, and the rest are skipped.
# The 'else' acts as a fallback if no 'if' or 'elif' conditions are met.

print("\n--- Nested if statements ---")
age = 20
has_license = True

if age >= 18:
    print("Eligible to drive (age-wise).")
    if has_license:
        print("Driver is legally allowed to drive.")
    else:
        print("Driver needs to obtain a license.")
else:
    print("Not eligible to drive yet.")
# Nested 'if' statements allow for more specific conditions within broader ones.

print("\n--- Using logical operators with if ---")
is_sunny = True
is_warm = True

if is_sunny and is_warm:
    print("Perfect weather for outdoor activities!")
if is_sunny or not is_warm:
    print("Either sunny or not warm, or both.")
# Logical operators (and, or, not) combine or negate conditions for more complex checks.