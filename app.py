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
