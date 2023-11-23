from datetime import datetime, timedelta
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'pl_Pl')
now = datetime.now()
print(now)
print(now.year)
print(now.strftime("%B"))
print(now+timedelta(days=5))
print(now-timedelta(weeks=2))

year = datetime.strptime("1990-05-28","%Y-%m-%d")
age = now-year
print(age)

