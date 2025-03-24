# Basic Calculator Program

# Function to safely get a valid number from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

# Get numbers from the user
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

# Get operation from the user
operation = input("Enter an operation (+, -, *, /): ")

# Perform calculation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation! Please enter +, -, *, or /.")
