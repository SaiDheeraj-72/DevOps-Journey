Objective

To store student names and grades using a Python dictionary, update an existing student's grade, and display all student records.

Explanation

The program creates a dictionary where the student's name is the key and the grade is the value. Users can add multiple students, update grades, and display all records.

Python Code
student_grades = {}

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    student_grades[name] = grade

update = input("Do you want to update a grade? (yes/no): ")

if update.lower() == "yes":
    name = input("Enter student name to update: ")

    if name in student_grades:
        new_grade = input("Enter new grade: ")
        student_grades[name] = new_grade
    else:
        print("Student not found.")

print("\nStudent Grades")

for name, grade in student_grades.items():
    print(name, ":", grade)


#Expected Output

Enter the number of students: 3

Enter student name: Sai
Enter student grade: A

Enter student name: Dheeraj
Enter student grade: B

Enter student name: Chary
Enter student grade: A

Do you want to update a grade? yes

Enter student name to update: Dheeraj

Enter new grade: A

Student Grades

Sai : A
Dheeraj : A
Chary : A
