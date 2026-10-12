from datetime import datetime

today = datetime.now()

print(today.strftime("%d-%m-%Y"))
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%H:%M:%S"))
print(today.strftime("%A"))
print(today.strftime("%B"))


#Convert a string into a date using strptime()

from datetime import datetime

date_string = "15-08-2026"

date_object = datetime.strptime(date_string, "%d-%m-%Y")

print(date_object)
print("Year:", date_object.year)
print("Month:", date_object.month)
print("Day:", date_object.day)

#Calculate the difference between two dates

from datetime import date

start_date = date(2026, 1, 1)
end_date = date(2026, 10, 12)

difference = end_date - start_date

print("Total days:", difference.days)