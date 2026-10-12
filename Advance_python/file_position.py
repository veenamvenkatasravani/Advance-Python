with open("position.txt", "w+", encoding="utf-8") as file:
    file.write("Hello Python")
    print("Position after writing:", file.tell())

    file.seek(0)
    print("Position after seek:", file.tell())

    content = file.read()
    print("Content:", content)

    print("Position after reading:", file.tell())