try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program Finished")


# Output
Cannot divide by zero
Program Finished


# Explanation

Exception handling prevents a program from crashing due to runtime errors.
