# Python course for beginners
import math


course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])


course = "python \"programming\""  # escape command
print(course)

first = "Samuel"
last = "Perez"
full_name = first + " " + last
print(full_name)


full_name2 = f"{first} {last}"
print(full_name2)

# methods
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())  # rstrip  lstrip
print(course.find("pro"))
# if we get -1 means that the char wasnt exist or at least no exactly as we were specify
print(course.replace("p", "j"))
print("pro" in course)
# The difference between this expression and find its that this one return a boolean instead of a index
print("swift" not in course)

# Working with numbers
print(round(2.9))
print(abs(-2.9))
# (MATH FUNCTION)If we want to find all the functions we can find on Google
print(math.ceil(2.2))

# # input function
# x = input("x: ")
# # y = x+1  # with this expression we gonna have a problem because now the variable is identified as a string and we supposed to have it as a number
# y = int(x) + 1
# print(f"x:{x}, y:{y}")

# Conditonal statment
temperature = 1
if temperature > 30:
    print("Its Warm")
    print("Drink Water")
elif temperature > 20:
    print("I think that this weather its nice")
else:
    print("It's so Cold")


age = 22
if age >= 18:
    print("Elegible")
else:
    print("Not Elegible")


# Better code (Simply)
age2 = 7
message = "Elegible" if age2 >= 18 else "Not Elegible"  # Ternary Operator

# Logical Operators
high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print("Elegible")
else:
    print("Not Elegible")

if high_income and good_credit and not student:
    print("Elegible")


# age should be between 18 and 65
age = 17
# if age >= 18 and age <= 65: # We can Write this expression Cleaner
if 18 <= age < 65:
    print("age it's between parameters")
else:
    print("No NO ")

# For Loops
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

succesfull = True
for number in range(1, 4):
    if succesfull:
        print("succesfull")
        break
else:
    print(f"Attempted {number} times  and does not working ")


# Nested Loops

for x in range(1, 6):
    for y in range(1, 4):
        print(f"{x}, {y}")

# Complex types
print(type(range(5)))  # Type Range (complex Type)

# While Loops
# number = 100
# while number > 0:
#     print(number)
#     # number = number // 2
#     number //= 2  # cleaner way to write the same

# command = ""
# while command.lower() != "quit":
#     command = input(">>")
#     print("Echo", command)


# # Infinite Loops
# command
# while True:
#     command = input(">")
#     print("Echo", command)
#     if command.lower() == "quit":
#         break


# Exercise
counter = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        counter = counter + 1

print(f"We have {counter} even numbers on this range")


# Own Functions
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Samuel", "Perez")
greet("Rojelio", "Lopez")

# Types of Functions
# On Programming we have two types of Functions
# 1-Perform a task
# 2-Return a Value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("sam")
# file = open("content.txt", "w")
# file.write(message)


def increment(number, by):
    return number + by


# result = increment(2, 1)
# print(result)

# print(increment(2, 1))
# Keyword Argument
print(increment(2, by=1))

#####################################


def multiply(*numbers):
    total = 1
    for number in numbers:
        # total = total * number
        total *= number  # cleaner option
    return total


print(multiply(2, 3, 4, 5))
