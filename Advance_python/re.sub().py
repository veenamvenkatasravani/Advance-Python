import re

text = "Python is difficult. Python needs practice."

result = re.sub("Python", "Programming", text)

print(result)

#Match a pattern at the beginning

import re

text = "Python programming"

result = re.match(r"Python", text)

if result:
    print("Matched at the beginning")
else:
    print("No match at the beginning")