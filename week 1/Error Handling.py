#Error Handling :  Errors (exceptions) can crash a program. We handle them using try-except.

try:
    x = 10 / 0  # Error: Division by zero
except ZeroDivisionError:
    print("Cannot divide by zero!")


#Handling Multiple Exceptions.

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
