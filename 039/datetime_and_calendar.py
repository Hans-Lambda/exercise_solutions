from datetime import datetime, timedelta
import calendar


# https://www.dataquest.io/blog/python-datetime-tutorial/#:~:text=Python%20datetime%20Classes&text=datetime%20%E2%80%93%20Allows%20us%20to%20manipulate,minute%2C%20second%2C%20microsecond).
# https://strftime.org/
# https://www.justintodata.com/manipulate-date-and-time-in-python/


date = "March 28 2011, 16:12"

# convert to datetime object

converted_date = datetime.strptime(date, "%B %d %Y, %H:%M")

print(converted_date)

year = converted_date.year + 2

# timedelta

time_1 = datetime(day=14, month=6, year=2022, hour=9, minute=0)
time_2 = datetime(day=14, month=6, year=2022, hour=16, second=15)

print(time_2 - time_1)

# calculate time in the future

time_3 = datetime(day=14, month=6, year=2022)
print(time_3)
print(time_3 + timedelta(hours=48))

# formatting

date_string = time_3.strftime("%m/%d/%Y, %H:%M:%S")

print(date_string)
print(type(date_string))


# calendar

calendar.setfirstweekday(0)
print(calendar.month(2044, 1))
print(calendar.firstweekday())

# timestamps

timestamp = time_3.timestamp()
print(time_3)
print(f"Timestamp: {timestamp}")
converted_timestamp = datetime.fromtimestamp(timestamp)
print(converted_timestamp)
