file = open("demo.txt", "w", encoding="utf-8")
try:
    file.write("Learning Python")

finally:
    file.close()