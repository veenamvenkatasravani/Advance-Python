#python use pathlib module to work with file paths conveniently

from pathlib import Path

folder = Path("student_records")
folder.mkdir(exist_ok = True)

file_path = folder / "student.txt"

file_path.write_text(
    "Name: Sravani\nMarks: 90\n", encoding = "utf-8")

print("File exists:", file_path.exists())
print("File name:", file_path.name)
print("File extension:", file_path.suffix)
print("File content:")
print(file_path.read_text(encoding="utf-8"))