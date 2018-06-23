from datetime import date, timedelta
now = datetime.now()
delta = timedelay(days=1)
yesterday = now - delta
delta2 = timedelay(month=1)
month = now - delta2
print(now)
print(yesterday)
print(month)

date = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date, '%d.%m.%Y')
print(date_dt)