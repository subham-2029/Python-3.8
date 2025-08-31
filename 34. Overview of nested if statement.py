age = 25
has_special_offer = True

if age >= 18:  # Outer if: Check if the person is an adult
    print("You are old enough to order.")
    if has_special_offer:  # Inner if: Check for a special offer for adults
        print("You are eligible for a discounted drink!")
        drink_price = 5.00  # Discounted price
    else:
        print("No special offer available for you.")
        drink_price = 8.00  # Regular price
    print(f"Your drink will cost ${drink_price:.2f}.")
else:  # Outer else: If the person is not an adult
    print("You are too young to order an alcoholic beverage.")
    if age >= 10: # Inner if: Check if they can order a non-alcoholic drink
        print("You can order a juice or soda.")
        drink_price = 3.00
    else: # Inner else: If they are very young
        print("Please ask an adult to order for you.")
        drink_price = 0.00 # No drink ordered directly
    print(f"Your non-alcoholic drink will cost ${drink_price:.2f}.")

print("\nThank you for your order!")