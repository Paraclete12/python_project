# arihmetic Operators

a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.33
print(a // b)  # Floor division: 3
print(a % b)  # Modulus (remainder): 1
print(a ** b)  # Exponentiation (power): 1000

a = 100
b = 6

print(a + b)
print(a % b)
print(a - b)
print(a / b)
print(a // b)
print(a * b)
print(a ** b) 

a = 100 
b = 3
c = 7
print(c ** (b // a) / b)

#Comparison Operators

print(a > b)  # True
print(a < b)  # False
print(a == b)  # False
print(a != b)  # True
print(c > b)  #True

#Logical Operators

x = True
y = False

print(x and y)  # False (Both must be True)
print(x or y)   # True (At least one must be True)
print(not x)    # False (Reverses the value)

male = "chibuikem"
female = "paraclete"

print(male and female)

x = True
y = False

print(x and y)
print(x or y)
print(not y)

#Control Flow (Loops, Conditionals) 
#Conditionals (if, elif, else) Conditional statements help us make decisions.

age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
# senior citizen

age = 70

if age < 70:
    print("you are not a senior citizen.")
elif age == 70:
    print("you just become a senior citizen.")
else:
    print("you are a senior citizen.")

#Loops (for, while)  Loops let us repeat actions.
#for loop

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

male_names =["gabby", "zimuzo", "chibuikem", "onyeka",]

for male_name in male_names:
    print(male_name)

#while loop

count = 0

while count < 5:
    print(count)
    count += 1  # Increment count by 1

count = 5

while count > 1:
    print(count)
    count -= 1

#Loop Control Statements | break → Exit loop immediately | continue → Skip the current iteration 

for num in range(5):
    if num == 3:
        break  # Stops the loop when num is 3
    print(num)

for num in range(5):
    if num == 3:
        continue  # Skips 3 and continues
    print(num)

for num in range(7):
    if num == 6:
        break
    print(num)

for num in range(7):
    if num == 6:
        continue
    print(num)