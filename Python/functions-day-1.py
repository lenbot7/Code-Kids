"""
Functions and scope
Day 1
Lenny
"""

# This script prints "Hello, World!" to the console and defines a function to determine a grade based on user input.

print("Hello, World!")


# Define a function to determine the grade based on the input score.
def determine_grade():
    """
    Prompts the user to enter a grade and prints the corresponding letter grade.

    The function uses the following grading scale:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: 0-59
    """
    grade = int(input("Enter your grade: "))

    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")


# Call the function to determine the grade.
determine_grade()
