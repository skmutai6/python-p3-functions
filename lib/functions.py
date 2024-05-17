#!/usr/bin/env python3

def greet_programmer():
    print(f"Hello, programmer!")
greet_programmer()


def greet(name = "Friend"):
    print(f"Hello, {name}!")
greet("Friends")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()


def add(num1, num2):
    print(num1 + num2)
add(1, 2)

def halve(number):
    print(number/2)
halve(2)
