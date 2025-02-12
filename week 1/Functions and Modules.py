#Functions and Modules
#Functions: A function is a reusable block of code. |Defining and Calling a Function.


def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Calls the function

def greet(name):
    print(f"Hello, {name}!")

greet("paraclete")

#Function with Return Value

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

def add(y, x):
    return y + x

result = add(190, 20)
print(result) 

#Modules | A module is a Python file containing functions and variables that you can import.
#Using Built-in Modules

import math

print(math.sqrt(16))  # Square root of 16 -> 4.0

import math

print(math.sqrt(81))