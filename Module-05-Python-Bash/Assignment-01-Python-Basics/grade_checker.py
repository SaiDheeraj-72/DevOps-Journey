Objective

To determine the student's grade based on the marks entered by the user using conditional statements.

Explanation

This program accepts marks as input from the user. Using if-elif-else statements, it compares the entered marks with predefined grade ranges and prints the appropriate grade.

Python Code
student_count = int(input("Enter number of students: "))

while student_count > 0:
    marks = int(input("Enter the marks: "))

    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

    student_count -= 1


# Expected Output

Enter number of students: 5
Enter the marks: 95
Grade: A

Enter the marks: 85
Grade: B

Enter the marks: 75
Grade: C

Enter the marks: 65
Grade: D

Enter the marks: 35
Grade: F
