# Simple Calculator

# Accept two numbers from the user
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
floor_division = first_number // second_number
modulus = first_number % second_number
exponentiation = first_number ** second_number

# Display the results
print("\n=== Calculator Results ===")
print(f"Addition (+): {addition}")
print(f"Subtraction (-): {subtraction}")
print(f"Multiplication (*): {multiplication}")
print(f"Division (/): {division}")
print(f"Floor Division (//): {floor_division}")
print(f"Modulus (%): {modulus}")
print(f"Exponentiation (**): {exponentiation}")