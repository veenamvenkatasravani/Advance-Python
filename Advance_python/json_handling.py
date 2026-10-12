import json

student = {
    "name": "Sravani",
    "age": 22,
    "course": "Python",
    "passed": True
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))