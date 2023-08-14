#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    return num1 + num2
sum_result = add(1, 2)
print(sum_result)

def halve(number):
    return number / 2
halve_result = halve(4)
print(halve_result)
halve_result_invalid = halve(8)
print(halve_result_invalid)