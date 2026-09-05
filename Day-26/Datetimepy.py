
from datetime import date,time,datetime,timedelta
'''
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

dt,month,year = list(map(int,input("[YYY-MM-DD]").split("-")))


from datetime import time
t = time(23,6,5)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

from datetime import datetime
n = datetime.now()
print(n)
print(n.strftime('%d-%m-%y'))
print(n.strftime('%d-%m-%y %H:%M:%S'))
print(n.strftime('%d-%m-%y %H:%M:%S %P'))
print(n.strftime('%d %b %y %H:%M:%S %p'))
print(n.strftime('%d %B %y %H:%M:%S %p'))
print(n.strftime('%a, %d %d %B %Y %H:%M:%S %p'))
print(n.strftime('%A, %d %B %Y %H:%M:%S %p'))

from datetime import datetime
n = datetime.now()
print(n)
print(n.day)
print(n.month)
print(n.year)
print(n.weekday())
print(n.hour)
print(n.minute)
print(n.second)
print(n.strftime('%d-%m-%y'))
print(n.strftime('%d-%m-%y %H:%M:%S'))
print(n.strftime('%d-%m-%y %H:%M:%S %P'))
print(n.strftime('%d %b %y %H:%M:%S %p'))
print(n.strftime('%d %B %y %H:%M:%S %p'))
print(n.strftime('%a, %d %d %B %Y %H:%M:%S %p'))
print(n.strftime('%A, %d %B %Y %H:%M:%S %p'))
'''

t = date.today()
n = datetime.now()
t7 = t + timedelta(days=7)
t5 = t - timedelta(days=7)
n15 = n + timedelta(minutes=15)
print(t,t7,t5)
print(n,n15)
