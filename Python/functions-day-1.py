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


# Define a function to add two numbers and print the result.
def add(a, b):
    """
    Prints the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    """
    return a + b


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    float: The temperature in Celsius.
    """
    return (fahrenheit - 32) * 5.0 / 9.0


def settings(sound=100, graphics="high", text_size=13):
    print(f"Sound: {sound}")
    print(f"Graphics: {graphics}")
    print(f"Text Size: {text_size}")


# Call the function to determine the grade.
determine_grade()

print(add(5, 10))

print(fahrenheit_to_celsius(100))

settings(sound=50, graphics="medium", text_size=12)
