import re

text = "Python is easy. I am learning Python."

result = re.search("Python", text)

if result:
    print("Word found")
    print("Position:", result.start())
else:
    print("Word not found")

#Find all numbers

import re

text = "I have 2 laptops, 3 phones and 10 books."

numbers = re.findall(r"\d+", text)

print(numbers)

#Validate a 10-digit phone number

import re

phone = input("Enter a 10-digit phone number: ")

pattern = r"^[0-9]{10}$"

if re.fullmatch(pattern, phone):
    print("Valid 10-digit format")
else:
    print("Invalid phone number format")

#e-mail-format validation

import re

email = input("Enter your email: ")

pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Email format looks valid")
else:
    print("Invalid email format")


#Extract email addresses from text

import re

text = """
Contact Ravi at ravi@example.com.
Contact Sravani at sravani@gmail.com.
"""

emails = re.findall(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    text
)

for email in emails:
    print(email)