"""
OOP intro
Day 2
Lenny
"""
# noinspection PyUnresolvedReferences
import this

import time

import random


def countdown():
    """
    Simple countdown.
    """
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("Blastoff!")


def guess_my_number():
    """
    Guess my number game.
    """
    number = random.randint(1, 100)
    guess = 0
    attempts = 0
    while guess != number:
        guess = int(input("Guess my number (1-100): "))
        attempts += 1
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
    print(f"You guessed it in {attempts} attempts!")


def main():
    countdown()
    guess_my_number()


if __name__ == "__main__":
    main()
