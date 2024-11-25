"""
Functions and scope
Day 1
Lenny
"""

# This script prints "Hello, World!" to the console, defines functions to determine a grade based on user input, add two numbers, convert Fahrenheit to Celsius, set settings, and add multiple numbers.

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
    Returns the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b


# Define a function to convert Fahrenheit to Celsius.
def fahrenheit_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    float: The temperature in Celsius.
    """
    return (fahrenheit - 32) * 5.0 / 9.0


# Define a function to set and print settings.
def settings(sound=100, graphics="high", text_size=13):
    """
    Prints the settings for sound, graphics, and text size.

    Parameters:
    sound (int): The sound level (default is 100).
    graphics (str): The graphics quality (default is "high").
    text_size (int): The text size (default is 13).
    """
    print(f"Sound: {sound}")
    print(f"Graphics: {graphics}")
    print(f"Text Size: {text_size}")


# Define a function to add multiple numbers.
def full_add(*args):
    """
    Returns the sum of all provided arguments.

    Parameters:
    *args (int or float): A variable number of arguments to be summed.

    Returns:
    int or float: The sum of all provided arguments.
    """
    return sum(args)


def main():
    # Call the function to determine the grade.
    determine_grade()

    # Print the result of adding two numbers.
    print(add(5, 10))

    # Print the result of converting 100 Fahrenheit to Celsius.
    print(fahrenheit_to_celsius(100))

    # Call the settings function with custom values.
    settings(sound=50, graphics="medium", text_size=12)


if __name__ == "__main__":
    main()
