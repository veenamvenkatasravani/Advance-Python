try:
    with open("unknown.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You do not have permission to read the file.")

except OSError as error:
    print("File operation failed:", error)

finally:
    print("File operation finished.")