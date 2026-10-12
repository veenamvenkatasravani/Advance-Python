#create a binary file
#Binary mode is used for files such as images, PDFs, and other non-text data.

with open("data.bin", "wb") as file:
    file.write(b"Hello Python")

#Read the binary file

with open("data.bin", "rb") as file:
    content = file.read()

print(content) 