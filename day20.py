# Day 20 – Python datetime Module
# The datetime module lets us work with dates and times easily in Python.

import datetime  # Import the datetime module

# 1. Getting the current date and time
current_dt = datetime.datetime.now()
print("Current date and time:", current_dt)

# 2. Getting only the date
today_date = datetime.date.today()
print("Today's date:", today_date)

# 3. Creating a custom date
# datetime.date(year, month, day)
my_birthday = datetime.date(2002, 5, 14)
print("My birthday:", my_birthday)

# 4. Formatting dates into strings (strftime)
formatted_date = current_dt.strftime("%d-%m-%Y %H:%M:%S")
# %d = day, %m = month, %Y = year, %H = hour, %M = minute, %S = second
print("Formatted date and time:", formatted_date)

# 5. Parsing a string into a date (strptime)
date_string = "15/08/2025"
parsed_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
print("Parsed date object:", parsed_date)

# 6. Date arithmetic
# Adding days using timedelta
future_date = today_date + datetime.timedelta(days=10)
print("Date after 10 days:", future_date)

# Subtracting days
past_date = today_date - datetime.timedelta(days=5)
print("Date 5 days ago:", past_date)

# 7. Getting individual parts of a date
print("Year:", today_date.year)
print("Month:", today_date.month)
print("Day:", today_date.day)

# 8. Real-world use case: Simple reminder
meeting_date = datetime.date(2025, 8, 15)
if today_date == meeting_date:
    print("Reminder: You have a meeting today!")
else:
    print("No meeting today.")
