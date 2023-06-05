"""myStr = 'hello'
print(id(myStr))
print(type(myStr))
print(myStr)

zminna_ryadok = '''hello1
                hello2
                 hello3'''
print(zminna_ryadok)

a='pyton'
print(a[0])
print(a[1])
print(a[-1])
print(a[len(a)-1])

a="Галантная беседа», возможно, одно из самых обсуждаемых произведений Терборха, Галантная содержание которого до настоящего времени неясно и является предметом дискуссий"
print(a.capitalize())#первий знак большой ост нижний рег
print(a.lower()) #нижний рег
print(a.upper()) # верхний регистер
print(a.title())  #первіе бук слов в верх рег
print(a.swapcase()) # противолежний регистр

print(a.count('Галантная'))# кол во вхождений фрагмента в рядочке
print(a.count('Галантная',20,65))
print(a.count('Галантная',20))

print(a.find('возможно')) # индекс первого вхождения в рядке
print(a.find('возможно',20))

print(a.index('возможно'))# индекс первого вхождения в рядке кщо не має то иде помилка

print(a.rfind('Галантная'))# индекс последнего вхождения задданного слова в рядке
print(a.rfind('Галантная',20,65))

print(a.rindex('Галантная'))"""

"""a="Галантная беседа», возможно, одно из самых обсуждаемых произведений Терборха, Галантная содержание которого до настоящего времени неясно и является предметом дискуссий"
zminna = input('введить слово')
print('данное слово попадаеться в тексте',a.count(zminna),'раз')
"""

"""
a="Галантная беседа», возможно, одно из самых обсуждаемых произведений Терборха, Галантная содержание которого до настоящего времени неясно и является предметом дискуссий"
print(a.startswith('г'))
print(a.startswith('Г'))
print(a.startswith('Галантная'))

print(a.endswith('"')) # заканчиваеться ли строка даннім символом
print(a.endswith('"',0,90))
print(a.endswith('.',0,90))"""

"""stroka= 'Python2023'
print(stroka.isalnum()) # проверка ряд содержит только числа и буквы
print(stroka.isalpha()) # проверка ряд содержит только буквы
print(stroka.isdigit()) # проверка ряд содерж только числа"""

"""a=input('enter 1 num')
b=input('enter 2 num')
if a.isdigit()== True and b.isdigit()==True:
    c= int(a)+int(b)
    print(c)
else:
    print('введено не коректное значение')"""
"""a="Галантная беседа», возможно, одно из самых обсуждаемых"
print(a.islower())# чи всі ел рядка в нижньому рег
print(a.istitle())# перевір чи кож слов поч з вел б
print(a.isupper()) # перевір чи всі ел в верх рег

a= 'Pyt\thon'
print(a.center(30))
print(a.center(30,'*'))
print(a.expandtabs(tabsize=8)) # задаем сколько пробелов в \t
print(a.ljust(30))
print(a.ljust(30,'@'))
print(a.rjust(30,'0'))
"""
"""
stroka='Python-cool!'
print(stroka[1:3])
print(stroka[-5:-2])
print(stroka[-5:11])
print(stroka[:6])
print(stroka[0:6])
print(stroka[-5:])


stroka_1='0123456789'
print(stroka_1[2:10:2])
print(stroka_1[9:2:-2])
print(stroka_1[::-1])
print(stroka_1[5::2])
print(stroka_1[-1::-2])
print(stroka_1[:len(stroka_1):3])
"""

"""#a= '\n \t \\'
a= '\\n \t \\'
print(a)
z=r'\n - newline'
print(z)"""

"""day = 11
month = 'Квітень'
print('today{}.{}'.format(day,month))
print('today {day}.{month}'.format(month=month,day=11))"""

year = 2023
name = 'Nastya'
print(f'Hello{name}')
print(f'Hello{name*2}')
print(f'Hello{len(name)}. now is{year}')
print(f'Hello{name:^30}')
#^ выравниване по центру
# <- выравнивание за левым кра
# >- выравнивание по правому краю

