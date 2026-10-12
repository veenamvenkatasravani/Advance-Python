import json

data = '''
{
    "employee": {
        "name": "Sravani",
        "role": "Python Developer",
        "salary": 30000
    }
}
'''

result = json.loads(data)

print(result["employee"]["name"])
print(result["employee"]["role"])
print(result["employee"]["salary"])