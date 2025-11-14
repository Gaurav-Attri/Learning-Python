# Creating a file:
# f = open("myfile.txt", "w")
# f.write("This is line 1\nThis is line 2\nThis is line 3\n")
# f.writelines(["Hello sir, ", "You are now about to witness the power of street knowledge"])

# Reading from a file
# f = open("myfile.txt", "w+")
# f.write("This is line 1\nThis is line 2\nThis is line 3\n")
# f.writelines(["Hello sir, ", "You are now about to witness the power of street knowledge"])
# f.seek(0)
# print(f.read())
# f.close();

# Using context-manager to open files safely and always free up resources after using them
with open("myfile.txt", "r") as f:
    data = f.read()
    print(data)