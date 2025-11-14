# Simple conditional expressions
# age = int(input("Please enter your age: "))
# if(age >= 18 and age <= 100):
#     print("You can vote")
# elif(age < 18 and age > 0):
#     print("You can't vote")
# else:
#     print("Invalid age")

# Ternary expression
# age = int(input("Please enter your age: "))
# canVote = "You can vote" if age >= 18 and age <= 100 else "You can't vote" if age < 18 and age > 0 else "Invalid age"
# print(canVote)

# while loop
# i = 0
# while i < 10:
#     print("i is:", i)
#     i += 1

# for loop with range, and unpacking (unpacking is just destructuring)
# for i in range(2, 5, 2):
#     print("i is:", i);

# points = [[1, 2], [2, 3]]
# for x, y in points:
#     print(x, y)

# else clause with loops, Loop else = runs only if the loop wasn’t broken out of.
for i in range(5):
    if(i == 10):
        print("Loop interrupted")
        break
else:
    print("Loop not interrupted")