
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose an operator: +, -, *, /")
    operator = input("Enter operator: ")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator selected.")
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
finally:
    print("Calculation complete. Thank you for using the calculator!")

