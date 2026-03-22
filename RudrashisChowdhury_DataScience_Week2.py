import numpy as np

# Tasks 1: Basic Operations

# Accepts two integers inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Performs the following using arithmetic operators
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2
modulus = num1 % num2
exponent = num1 ** num2

# Print the results using f-string
print(f"Add: {num1} + {num2} = {add}")
print(f"Subtract: {num1} - {num2} = {subtract}")
print(f"Multiply: {num1} * {num2} = {multiply}")
print(f"Divide: {num1} / {num2} = {divide}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponential: {num1} ** {num2} = {exponent}")

# Tasks 2: Working with List and Arrays

# List containing at least 10 numbers
numbers = [10, 2, 15, 37, 22, 88, 66, 99, 13, 78]
print(f"Original List: {numbers}")

# Print the length of the list
print(f"Length of the List: {len(numbers)}")

# Find the Maximum and Minimum Value
print(f"Maximum Value: {max(numbers)}")
print(f"Minimum Value: {min(numbers)}")

# Add a new element to the list
numbers.append(25)

# Remove one element to the list
numbers.remove(2)

# Show the results
print(f"Changed List: {numbers}")

# Convert the list to NumPy Array
arr = np.array(numbers)

# Calculate Mean, Median and STD of the NumPy Array
print(f"Mean: {np.mean(arr)}")
print(f"Median: {np.median(arr)}")
print(f"Standard Deviation: {np.std(arr)}")

# Task 3: Dictionaries and Sets

student = {
    "name": "Rudrashis Chowdhury", 
    "age": 24, 
    "course": "Artificial Intelligence and Machine Learning", 
    "marks": 69.5
}

# print each key and value pair using loop
for key, value in student.items():
    print(f"{key}: {value}")

# Add a new key called grade with a value of choice
student["grade"] = "A"

# Show the result
for key, value in student.items():
    print(f"{key}: {value}")

# set of unique courses and display it.
courses = {"Python", "Data Science", "AI", "Python"}
print(f"\nUnique Courses: {courses}")

# set operarion -- union, intersection, and difference
set1 = {"Python", "AI", "ML"}
set2 = {"AI", "ML", "Data Sciences"}

print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")

# Task 4: File Handing

# Write the data into the file (Name, course, marks of at Least 5 students)
with open("student_data.txt", "w") as file:
    file.write("Rohit,Python,65\n")
    file.write("Sneha,Data Science,90\n")
    file.write("Mohini,ML,85\n")
    file.write("Raj,AI,60\n")
    file.write("Neha,ML,85\n")

# Read the file and display only those students whose marks are above 75
with open("student_data.txt", "r") as file:
    line = file.read()
    for line in file:
        name, course, marks = line.strip().split(",")
        if int(marks) > 75:
            print(f"Name: {name}\nCourse: {course}\nMarks: {marks}")