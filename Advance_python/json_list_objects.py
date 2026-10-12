import json

json_data = '''
[
    {"id": 1, "name": "Ravi", "marks": 85},
    {"id": 2, "name": "Sravani", "marks": 92},
    {"id": 3, "name": "Priya", "marks": 78}
]
'''

students = json.loads(json_data)

for student in students:
    print(student["name"], student["marks"])