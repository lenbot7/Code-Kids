"""
OOP Learning
Day 2
Lenny
"""
import random


class Pet:
    def __init__(self, name, pet_type, breed, age=0, gender="Unknown"):
        self.name = name
        self.pet_type = pet_type
        self.breed = breed
        self.age = age
        self.gender = gender

    def eat(self):
        food = ["kibble", "wet food", "treats", "raw meat", "cooked meat", "fish", "milk", "water", "vegetables",
                "fruit", "bones"]
        eating_food = random.choice(food)
        print(f"{self.name} is eating {eating_food}.")


class Address:
    def __init__(self, street, number, postcode, city, country="UK"):
        self.street = street
        self.number = number
        self.postcode = postcode
        self.city = city
        self.country = country


class Person:
    def __init__(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address


goose = Pet("Goose", "Cat", "Tabby", 3, "Male")
pip = Pet("Pip", "Dog", "Unknown", 1, "Male")
home = Address("High Street", 1, "AB1 2CD", "London")
lenny = Person("Lenny", "Kay", 30, home)
goose.eat()
pip.eat()
