#File handling means using a Python program to work with files stored on your computer.

#File handling is an important topic in Python. It allows us to create, open, read, write, append, and manage files using Python programs.

#Python program
#Creates, reads, or updates information

#Text file — students.txt
#Stores information on your computer for later use


file = open("sample.txt", "w")

file.write("Hello Sravani")
file.close()

print("File created successfully")