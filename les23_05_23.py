"""import datetime

dates=datetime.datetime(2023,5,23,hour=19,minute=25,second=53)
print(dates)
print(type(dates))

print(f'metod time-{dates.time()}\n {type(dates.time())}')
dat_1=datetime.date(2021,9,24)
time_1=datetime.time(5,8,48)
print(dat_1)
print(time_1)

date_and_time=datetime.datetime.combine(dat_1,time_1)
print(date_and_time,type(date_and_time))
print(f'new date={dat_1.replace(2022)}')
print(f'old date={dat_1}')"""
"""
import datetime
date_now=datetime.datetime.now()
date_today=datetime.datetime.today()
date_date=datetime.date.today()
print(f'date_now = {date_now}')
print(f'date_today = {date_today}')
print(f'date_date = {date_date}')

print(f'time now = {date_now.time()}')

#weekday 0-6 0=monday 6 = sunday
#isoweekday 1-7 

date_for_now=datetime.datetime.now()
print(f'weeday() = {date_for_now.weekday()}')
print(f'isoweekday() = {date_for_now.isoweekday()}')"""

# %A gовна назва дня тижня
# %B повна назва місяця
# %d день місяцяяя(01,31)
# %H година(24 год формат)
# %m номер місяця
# %M число хвилин
# %S число секунд
# %x дата
# %X час
# %Y рік
"""
import datetime

date_now=datetime.datetime.now()
print(f'date time to str = {date_now.strftime("%d.%m.%Y %H:%M %A")}')

date_str='28/09/2021 11:20'
date_str_res=datetime.datetime.strptime(date_str,'%d/%m/%Y %H:%M')
print(f'str to datetime = {date_str_res}')"""

"""import  datetime
date_now=datetime.datetime.now()
date=datetime.datetime(day=20,month=8,year=2020)
print(date_now-date)"""

"""import  datetime
date_now=datetime.datetime.now()
print(f'date now = {date_now}')
delta=datetime.timedelta(days=20,hours=8,weeks=4)
print(f'delta= {delta}')
print(date_now+delta)
a=date_now+delta
print(a.strftime("%d.%m.%Y "))"""

"""

import  datetime
a= int(input('Яку інформацію треба надати:\n 1- поточна дата\n2-день тижня\n3-дізнатися яка зараз година\n4-дізнатися скільки днів до потрібної дати\n5-дізнатися який день буде через н-днів\n'))
if a==1:
    date_now = datetime.datetime.now()
    print(f'сьогодні {date_now.strftime("%d.%m.%Y ")}')
elif a==2:
    date_now = datetime.datetime.now()
    print(f'сьогодні {date_now.strftime(" %A")}')
elif a==3:
    date_now = datetime.datetime.now()
    print(f'зараз {date_now.strftime("%H:%M")}')
elif a==5:
    z=int(input('Введить кількість днів: '))
    date_now = datetime.datetime.now()
    delta = datetime.timedelta(days=z)
    g = date_now + delta
    print(g.strftime("%d.%m.%Y "))
elif a==4:
    z=str(input('Введить дату у вигляді ДД/ММ/РРРР: '))
    date_now = datetime.datetime.now()
    date_str_res = datetime.datetime.strptime(z, '%d/%m/%Y')
    rez=date_str_res-date_now
    print('До ведденої дати',rez,'днів')
else:
    print('Помилка')"""


"""import os
path=os.path.normcase('C:/Windows/Web')
path1='C:\Windows\Web'
path2='C:\\Windows\\teb'
path3=r'C:\\Windows\\teb'
for path,dirnames,filenames in os.walk(path):
    print(f'path - {path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames - {filenames}')"""
"""
cor='C:\\'
dir1=input('enter folder')
dir2=input('enter folder')
path=os.path.join(cor,dir1,dir2)
for path,dirnames, filenames in os.walk(path):
    print(f'path -{path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames - {filenames}')"""


"""import os
path= os.path.normpath('new_dir')
os.mkdir(path)"""

"""
import os
path= os.path.normpath('new_dir')
os.rmdir(path)"""


"""
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text =='день':
        date_now = datetime.datetime.now()
        data=date_now.strftime("%d.%m.%Y ")
        bot.send_message(message.chat.id, data)"""