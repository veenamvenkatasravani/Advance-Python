import json

data = '{"name": "Sravani", "age": }'

try:
    result = json.loads(data)
    print(result)

except json.JSONDecodeError as error:
    print("Invalid JSON data!")
    print(error)