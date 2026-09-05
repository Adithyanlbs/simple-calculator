# Simple Calculator - Day 1 Assignment

print("=== Simple Calculator ===")

while True:
    try:
        # Accept two numbers from the user
        first_number = float(input("\nEnter the first number: "))
        second_number = float(input("Enter the second number: "))

        # Display available operators
        print("\nOperators: +  -  *  /  //  %  **")
        operator = input("Choose an operator: ").strip()

        # Perform the selected operation
        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            if second_number == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = first_number / second_number

        elif operator == "//":
            if second_number == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = first_number // second_number

        elif operator == "%":
            if second_number == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = first_number % second_number

        elif operator == "**":
            result = first_number ** second_number

        else:
            raise ValueError("Invalid operator. Please choose from +, -, *, /, //, %, **.")

        # Display the result
        print(f"\nResult: {result}")

    except ValueError as error:
        print(f"\nError: {error}")

    except ZeroDivisionError as error:
        print(f"\nError: {error}")

    # Ask whether the user wants to continue
    again = input("\nDo you want to continue? (y/n): ")

    if again.lower() != "y":
        print("Goodbye!")
        break
