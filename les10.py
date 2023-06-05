#m=lambda a,d:a/d
#print(m(4,2))

"""mult=lambda a,b,c:a*b*c
print(mult(5,2,9))
result=mult(5,2,9)
print(result)

def multdef(a,b,c):
    return a*b*c
print(multdef(5,2,9))
result=multdef(5,2,9)
print(result)"""

"""import math

abs=lambda a,b:math.sqrt(a*a + b*b) #корень квадратній из вираза в дужках
result=abs(9,7)
print(result)

def abs_def(a,b):
    return math.sqrt(a*a + b*b)
res=abs_def(9,7)
print(res)"""

"""import random
spysok=[lambda :random.random(),
        lambda :random.random(),
        lambda :random.random()]
for i in spysok:
    print(i())"""

"""cort=(lambda x:x*2,
      lambda x:x*3,
      lambda x:x*5)

for i in cort:
    print(i(2))

for i in cort:
    print(i('qwerty'))"""
"""
slovnyk={1:(lambda :print('Понеділок')),2:(lambda :print('Вівторок')),
         3:(lambda :print('Середа')),4:(lambda :print('Четвер')),
         5:(lambda :print('Пятниця'))}
answer=int(input('Число від 1до 5'))
try:
    slovnyk[answer]()
except KeyError:
    print('невірно задані данні')"""
"""
import math

area={'circle':(lambda r:math.pi*r*r),
      'rectangle':(lambda a,b,:a*b),
      'trap':(lambda a,b,h:(a+b)*h/2.0)}

answer=input('Введите фигуру')
if answer.lower()=='circle':
    answer1=int(input('задайте х'))
    print('Площа круга=', area['circle'](answer1))
# .. и тд 'rectangle'  'trap'
print('Площа круга=',area['circle'](2))
print('Пл трикутника=',area['rectangle'](10,13))
print('Пл трапеції = ',area['trap'](7,5,3))"""
"""
summa=lambda a=1,b=2,c=3:a+b+c

print(summa())
print(summa(5))         #ставит 5 на место а=1 ост остаеться как раньше b=2,c=3
print(summa(10,20))     # a=10,b=20,c=3
print(summa(10,20,25))  #a=10,b=20,c=25
"""

"""import random
def randomNum():
    n=random.random()
    res=lambda :int(n*100)
    return res()

print(randomNum())"""
"""
mult1=lambda a,b,:a+b
mult2=lambda a,b,:a-b
mul3t=lambda a,b,:a/b
mult4=lambda a,b,:a*b
mult5=lambda a:a*a
sho_rob= input('Оберить що рахуемо:1 (+), 2(-), 3(/),4(*), 5(квадрат числа')
if sho_rob == '1':
    z1=int(input('Задайте перше число'))
    z2=int(input('Задайте друге число'))
    print(mult1(z1,z2))
elif sho_rob == '2':
    z1=int(input('Задайте перше число'))
    z2=int(input('Задайте друге число'))
    print(mult2(z1,z2))
elif sho_rob == '3':
    z1=int(input('Задайте перше число'))
    z2=int(input('Задайте друге число'))
    print(mult3(z1,z2))
elif sho_rob == '4':
    z1=int(input('Задайте перше число'))
    z2=int(input('Задайте друге число'))
    print(mult4(z1,z2))
elif sho_rob == '5':
    z1=int(input('Задайте перше число'))
    print(mult5(z1))"""

"""max=(lambda a,b: a if a>b else b)
print(max(23,70))
print(max(21,4))

min=(lambda a,b,c: a if(a<=b) and (b<=c) else (b if (b<=a) and (b<=c) else c))
print(min(21,34,59))
print(min(57,15,2))
"""
"""
def mnoj_dva(x):
    return x*2

spysok=[1,5,6,8,9,7,3]
spysok2=list(map(mnoj_dva,spysok))
print(spysok2)

spysok3=list(map((lambda x:x*2 ),spysok))
print(spysok3)"""


"""cort=(2.88,-5.97,9.87)
cort2=tuple(map((lambda x:int(x)), cort))
print(cort2)"""

"""cort = ('qwert','asd','zxcvb','qwe')   # фильтруем и запис в новий кортеж данніе длина которіх равна 3
cort2= tuple(filter((lambda x:len(x)==3),cort))
print(cort2)
"""
"""spysok=[1,2,3,4,5,6,7,8,9,10,58,90,47,21]
spysok2=list(filter((lambda x:(x>=10)and(x<=60)),spysok))
print(spysok2)"""

"""import re
spysok1='bob anna alex bob'

vyraz=re.compile('bob')
vyraz2=re.compile('qwe')
match1=vyraz.search((spysok1))#щет первое попавщее значение
print(match1)
match2=vyraz.search(spysok1)#если значение не нашли то нон
print(match2)
match3=vyraz.finditer(spysok1) # щев все збіги
for i in match3:
    print(f'match_1 -{i} ')

match24=vyraz.findall(spysok1)#знайти всі збіги та помістити їх в список
print(match24)
print(len(match24))

spysok2='abc cds qwe'
poisk=re.compile('qwe')
new=poisk.sub('hello',spysok2) # замена на др значение
print(new)"""

"""import re
rechennya='о всім вопр писати на пошту qwert@gmail.com або asdfg@gmail.com або zxcvb@gmail.com'
emails=re.findall(r'[\w]+@[\w]',rechennya)
# \w проверяет есть ли ел состоящ из цифрі букви и _
for i in emails:
    print(i)"""


"""
import tkinter as tk
import re
loggin_patern=re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
passw=re.compile(r"^\w{8,16}$")
# ^ єто знак початка рядка
root=tk.Tk()
root.geometry('400x250+700+500')
root.resizable(False,False)
def logining():
    pass
login_lab=tk.Label(root, text='Login', font=('Arial',14), padx=50)
pasw_leb=tk.Label(root, text='Login', font=('Arial',14), padx=50)

root.grid_columnconfigure(0, minsize=150)
login_lab.grid(column=0, row=0)
root.mainloop() # зявлення вікна"""


"""var_1=5
def func():
    global var_1
    print(f'var_1=  {var_1}')
    var_1 = 10
func()
print(var_1)"""
"""
var_1 = 5

def func_3():
    var_1 = 10
    def func_4():
        print(var_1)
    func_4()
func_3()
print(var_1)
"""

