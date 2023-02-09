# import datetime
# print(dir(datetime))

from datetime import datetime
now = datetime.now()
print(now)
date = now.day
month = now.month
year = now.year

print(date, month, year)

new_year = datetime(2023, 1, 1)
print(new_year)

date_string = "9 Feb, 2023"
print("date_string=", date_string)


from datetime import time

a = time()
print("a = ", a)

b = time (10, 30, 50)
print("b=", b)

c = time(hour=10, minute=40, second=20)
print("c=", c)