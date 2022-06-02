# from datetime import datetime
# d = datetime(2020, 12, 25)
# if d.weekday() > 4:
#     print 'Given date is weekend.'
# else:
#     print 'Given data is weekday.'
# Monday -> 0
# Tuesday -> 1
# Wednesday -> 2
# Thur -> 3
# Friday -> 4
# Saturday -> 5
# Sunday -> 6
import datetime
# UTC -- 00:00 (Greenwhich)
# +2 (Berlin)
# +1 (UK)
# -5 New York (EST)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def isweekend(date=datetime.datetime.now()):
    if days[date.weekday()] == 'Saturday' or days[date.weekday()] == 'Sunday':
    # also acceptible
    # if date.weekday() > 4:
    # if date.weekday() == 5 or date.weekday() == 6:
        return True
    return False

def isweekend_version2(date=datetime.datetime.now()):
    return date.weekday() > 4

print(isweekend(datetime.date(2021, 8, 6)))
print(isweekend(datetime.date(2021, 8, 7)))
print(isweekend(datetime.date(2021, 8, 8)))
print(isweekend(datetime.date(2021, 8, 9)))
print("@@@@@@")
print(isweekend_version2(datetime.date(2021, 8, 6)))
print(isweekend_version2(datetime.date(2021, 8, 7)))
print(isweekend_version2(datetime.date(2021, 8, 8)))
print(isweekend_version2(datetime.date(2021, 8, 9)))

# How to use the "default" value set originally in the function definition
print(isweekend())