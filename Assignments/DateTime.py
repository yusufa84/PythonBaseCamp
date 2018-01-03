import datetime

t = datetime.time(4,25,30)
print(t)
print(t.hour)

print(datetime.time.min)
print(datetime.time.max)

today = datetime.date.today()
print(today.isoweekday())
print(today.timetuple())

d1 = datetime.date(2018,1,3)
print(d1)

d2 = d1.replace(year = 2017)
print((d1-d2))