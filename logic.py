from datetime import datetime
import calendar

arr = []
fine = 0
f_day = 15
f_month = 500
f_year = 10000


def add_date(d):
    return datetime.strptime(d, '%d %m %Y')


def diff(end, start):
    years = end.year - start.year
    months = end.month - start.month
    days = end.day - start.day
    if days < 0:
        months -= 1
        days += calendar.monthrange(start.year, start.month)[1]
    if months < 0:
        years -= 1
        months += 12
    return str(str(days) + ' ' + str(months) + ' ' + str(years))


for _ in range(2):
    arr.append(add_date(input()))

dt = diff(arr[0], arr[1])
print(dt)
ad = [int(x) for x in dt.split(' ')]
print(ad)

if ad[0] > 0:
    fine += ad[0] * f_day
if ad[1] > 0:
    fine += ad[1] * f_month
if ad[2] > 0:
    fine += ad[2] * f_year

print(fine)
