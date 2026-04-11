# Step 1: Display a heading for the calculator
print("Welcome to the Simple Calculator!")

# Step 2: Start a loop so the calculator runs continuously
while True:

    # Step 3: Use try block to handle possible errors
    try:
        # Step 4: Take first number input from the user
        num1 = float(input("Enter first number: "))

        # Step 5: Take operator input (+, -, *, /)
        operator = input("Enter operator (+, -, *, /): ")

        # Step 6: Take second number input from the user
        num2 = float(input("Enter second number: "))

        # Step 7: Check if operator is '+' and perform addition
        if operator == '+':
            result = num1 + num2
            print("Result:", result)

        # Step 8: Check if operator is '-' and perform subtraction
        elif operator == '-':
            result = num1 - num2
            print("Result:", result)

        # Step 9: Check if operator is '*' and perform multiplication
        elif operator == '*':
            result = num1 * num2
            print("Result:", result)

        # Step 10: Check if operator is '/' and perform division
        elif operator == '/':
            # Step 11: Before division, check if second number is zero
            if num2 == 0:
                # Step 12: If zero, display division by zero error message
                print("Error: Division by zero is not allowed.")
            else:
                # Step 13: If not zero, perform division and display result
                result = num1 / num2
                print("Result:", result)

        # Step 14: Handle invalid operator
        else:
            print("Error: Invalid operator. Please use +, -, *, or /.")

    # Step 15: Catch ValueError if user enters invalid number
    except ValueError:
        print("Error: Please enter valid numeric values.")

    # Step 16: Catch any unexpected error using Exception
    except Exception as e:
        print("Unexpected Error:", e)

    # Step 17: Ask user if they want to continue
    choice = input("Do you want to continue? (yes/no): ").lower()

    # Step 18: If user enters 'no', exit the loop
    if choice != 'yes':
        # Step 19: Display exit message and stop the program
        print("Exiting Calculator...")
        break