Objective

To create a text file and write data into it using Python file handling.

Explanation

The program opens a file named student.txt in write mode. If the file does not exist, Python creates it automatically. The write() function stores the text inside the file, and close() saves and closes it.

Python Code
file = open("student.txt", "w")

file.write("Hello, Welcome to Python File Handling!")

file.close()

print("Data written successfully.")

# Expected Output
    
Data written successfully.
