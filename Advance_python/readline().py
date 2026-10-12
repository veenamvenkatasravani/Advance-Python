#readline()-Read one line

with open("sample.txt", encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())

#readlines() — Read all lines into a list

with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)


#Read a file line by line
#For large files, iterating over the file is usually more memory-efficient than loading the entire file into memory.

with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

#strip() removes leading and trailing whitespace, including the newline at the end of each line.