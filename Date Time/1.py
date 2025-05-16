from datetime import *

today = date.today()
print("Today's date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("Weekday (0=Monday, 6=sunday):", today.weekday())
print("ISO Weekday (1=Monday, 7=Sunday):", today.isoweekday())


specific_date = date(2024, 2, 24)
print("specific date:", specific_date)

now=datetime.now()
print("current date and time:",now)

print("Years:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)       
