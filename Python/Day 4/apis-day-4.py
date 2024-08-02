"""
API Introduction
Lenny
Day 4
"""

import requests


def get_random_joke():
    """
    Get a random joke from the API.

    Returns:
    str: A random joke.
    """
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke = response.json()
    return joke["setup"] + " " + joke["punchline"]


print(get_random_joke())


def calculator():
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        return "Invalid input"
    operation = input("Enter the operation (+, -, *, /): ")
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        try:
            return n1 / n2
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"


print(calculator())
