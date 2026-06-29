# Python Basics for DevOps

## Introduction

Python is a high-level, interpreted, and general-purpose programming language known for its simple syntax and readability. It is one of the most popular programming languages used in DevOps, Cloud Computing, Data Science, Artificial Intelligence, Automation, and Web Development.

---

## Why Python in DevOps?

Python is widely used in DevOps because it simplifies automation and infrastructure management.

Some common use cases include:

* Automating repetitive tasks
* Creating and managing AWS resources
* Server administration
* Infrastructure automation
* Log file analysis
* Monitoring systems
* Configuration management
* Working with REST APIs
* CI/CD pipeline automation
* Cloud resource provisioning
* Writing deployment scripts

---

## Topics Covered

* Variables
* Data Types
* Input and Output
* Operators
* Conditional Statements (if, elif, else)
* Loops (for and while)
* Functions
* Modules
* Lists
* Tuples
* Dictionaries
* File Handling
* Exception Handling
* Compiler vs Interpreter
* Identifiers and Keywords
* PYPI Packages

---

## Python Data Types

Python supports several built-in data types.

* String (`str`)
* Integer (`int`)
* Float (`float`)
* Boolean (`bool`)
* List (`list`)
* Tuple (`tuple`)
* Dictionary (`dict`)
* Set (`set`)

Example:

```python
name = "Sai"
age = 21
cgpa = 9.11
is_student = True
```

---

## Conditional Statements

Conditional statements allow a program to make decisions based on conditions.

Python supports:

* if
* if-else
* if-elif-else
* Nested if

Example:

```python
age = 20

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## Loops

Loops execute a block of code repeatedly.

### For Loop

Used when the number of iterations is known.

### While Loop

Used when the condition controls the execution.

---

## Functions

Functions are reusable blocks of code that perform a specific task.

Python supports:

* Functions without arguments
* Functions with arguments
* Functions with return values

Benefits:

* Code reusability
* Better readability
* Easier maintenance

---

## Lists

Lists are ordered and mutable collections.

Example:

```python
fruits = ["Apple", "Banana", "Orange"]
```

Common operations:

* append()
* insert()
* remove()
* pop()
* sort()

---

## Tuples

Tuples are ordered but immutable collections.

Example:

```python
numbers = (10,20,30)
```

---

## Dictionaries

Dictionaries store data in key-value pairs.

Example:

```python
student = {
    "Name":"Sai",
    "Age":21
}
```

---

## File Handling

Python provides built-in support for reading and writing files.

Common modes:

* r → Read
* w → Write
* a → Append
* x → Create

Applications:

* Log analysis
* Report generation
* Configuration files
* Data processing

---

## Exception Handling

Exception handling prevents program crashes due to runtime errors.

Keywords used:

* try
* except
* else
* finally

Benefits:

* Improves program reliability
* Handles unexpected errors gracefully

---

## Modules

Modules are Python files containing reusable functions and classes.

Common built-in modules:

* math
* random
* os
* datetime
* sys

---

## PYPI Packages

Python Package Index (PyPI) is the official repository for third-party Python packages.

Popular DevOps packages:

* requests
* boto3
* flask
* paramiko
* docker
* kubernetes

Install packages using:

```bash
pip install package_name
```

Example:

```bash
pip install requests
```

---

## Compiler vs Interpreter

### Compiler

* Converts the entire program into machine code before execution.
* Faster execution after compilation.

Examples:

* C
* C++

### Interpreter

* Executes code line by line.
* Easier debugging.

Example:

* Python

---

## Identifiers

Identifiers are names given to variables, functions, classes, and objects.

Example:

```python
student_name
totalMarks
calculateSalary
```

Rules:

* Must start with a letter or underscore.
* Cannot start with a number.
* Cannot use Python keywords.

---

## Python Keywords

Keywords are reserved words with predefined meanings.

Examples:

* if
* else
* for
* while
* class
* def
* return
* import
* try
* except
* break
* continue

---

## Real-World DevOps Applications

Python is commonly used for:

* AWS Infrastructure Automation (Boto3)
* Server Health Monitoring
* Backup Automation
* Log File Processing
* Deployment Automation
* CI/CD Pipelines
* REST API Integration
* Kubernetes Automation
* Docker Automation
* Cloud Resource Management

---

## Learning Outcome

After completing this module, I am able to:

* Understand Python fundamentals.
* Write basic Python programs.
* Use conditional statements and loops.
* Create reusable functions.
* Work with lists, tuples, and dictionaries.
* Read and write files.
* Handle runtime exceptions.
* Import built-in and external modules.
* Install and use PyPI packages.
* Apply Python in DevOps automation.
