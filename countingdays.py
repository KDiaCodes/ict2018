import os
from datetime import date
import datetime


year = int(input("Enter your birthday first enter your birth year : "))
month = int(input("Enter your month now : "))
days = int(input("Enter your day now : "))

todayyear = datetime.datetime.today().year
todaymonth = datetime.datetime.today().month
todayday = datetime.datetime.today().day

f_date = date(year, month, days)
l_date = date(todayyear, todaymonth, todayday)
delta = l_date - f_date
print(delta.days)
input("Press enter to close")
os.system(r'start C:\Windows\System32\cmd.exe /c C:\Users\KENRICSA\Desktop\start.bat')
