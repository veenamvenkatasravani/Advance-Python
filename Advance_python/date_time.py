from datetime import datetime

current = datetime.now()

print("Current date and time:", current)
print("Date:", current.date())
print("Time:", current.time())

#Get date components separately

from datetime import datetime

today = datetime.now()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

print("Hour:", today.hour)
print("Minute:", today.minute)
print("Second:", today.second)