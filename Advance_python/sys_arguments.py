import sys

print("Program name:", sys.argv[0])
print("Arguments:", sys.argv[1:])

#using this command-- python sys_arguments.py Sravani Python 25


#Exit a program
import sys

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
    sys.exit()

print("Your age is :", age)