import os
path = "sample.txt"

if os.path.isfile(path):
    print("It is a file")

elif os.path.isdir(path):
    print("It is a folder")

else:
    print("Pathdoes not exist")


#join file paths safely

import os

folder = "data"
filename = "students.txt"

full_path = os.path.join(folder, filename)

print(full_path)