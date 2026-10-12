import json

student = {
    "name": "Sravani",
    "age": 22,
    "course": "CSE"
}

# Add a new key
student["city"] = "Hyderabad"

# Update an existing value
student["course"] = "Python"

# Remove a key
student.pop("age")

# Convert to JSON
json_data = json.dumps(student, indent=4)

print(json_data)