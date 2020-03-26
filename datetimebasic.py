import datetime

today = datetime.date.today()

print(today)

print(today.year)
print(today.month)
print(today.day)

print(today.weekday())

now = datetime.datetime.now()

print(now)

independence_day = datetime.date(year=2020, month=8, day=17)
print(independence_day)

time_delta = independence_day - today
print(time_delta)
print(time_delta.total_seconds())

print(independence_day.strftime('%d - %m - %Y'))

# August, 17 2020
print(independence_day.strftime('%B, %d %Y'))

us_independence_day_str = '2020-07-04'

us_independence_day = datetime.datetime.strptime(us_independence_day_str, '%Y-%m-%d')
print(us_independence_day)