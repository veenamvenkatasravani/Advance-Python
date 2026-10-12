file = open("sample.txt", "r")
content = file.read()

print(content)

file.close()

#read() — Read the entire file

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


#read() returns the remaining content as a single string.

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read(7))
