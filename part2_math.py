# Part 2: Multiplication and Division

# Ask the user to input two numbers
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Perform multiplication
multiplication_result = num1 * num2
print(f"The multiplication of {num1} and {num2} is: {multiplication_result}")

# Perform division, checking for division by zero
if num2 != 0:
    division_result = num1 / num2
    print(f"The division of {num1} by {num2} is: {division_result}")
else:
    print("Division by zero is not allowed.")
