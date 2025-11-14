# positional and keyword arguments
# def greet(name, age):
#     print(f"Hello {name}, who is {age} years old");

# greet("Gaurav", 23) # arguments passed by position, positional arguments
# greet(age=23, name="Gaurav") # arguments passed by keyword, keyword arguments (order doesn't matter)
# greet("gaurav", age=23); # keyword argument must follow positional arguments

# default arguments
# def greet(age, name="Gaurav"):
#     print(name, age);

# greet(12);
# greet(23, "Amit");

# Variable-length positional arguments
# def sum(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# print(sum(1))
# print(sum(1, 2))
# print(sum(1, 2, 3))

# Variale-length keyword arguments
# def printStudentDetails(**students):
#     for name, roll in students.items():
#         print(f"{name}, {roll}")

# printStudentDetails(student1="Gaurav", age1=23, student2="Ayush", age2=22)

# Lambda functions
# add = lambda x, y : (x+y)
# print(add(5, 6))
