#Завдання 1
#Користувач вводить з клавіатури номер дня тижня (1-7).
#Виведіть на екран назву дня тижня. Наприклад, якщо введено
#1, то на екрані з’явиться напис «Понеділок», 2 — вівторок і т. д.
try:
    day =int(input('Оберить номер дня тижня який треба назвати (1-7)- '))
    if day==1:
        print(day,'день тижня \n ПОНЕДІЛОК')
    elif day==2:
        print(day,'день тижня \n ВІВТОРОК')
    elif day==3:
        print(day,'день тижня \n СЕРЕДА')
    elif day==4:
        print(day,'день тижня \n ЧЕТВЕР')
    elif day==5:
        print(day,"день тижня \n П'ЯТНИЦЯ")
    elif day==6:
        print(day,'день тижня \n СУБОТА')
    elif day==7:
        print(day,'день тижня \n НЕДІЛЯ')
    else:
        print('Ви ввели не вірне значення.')
except:
    print('Ви ввели не вірне значення.')

#Завдання 2
#Користувач вводить з клавіатури номер місяця (1-12).
#Виведіть на екран назву місяця. Наприклад, якщо введено 1,
#то на екрані з’явиться напис «Січень», 2 — «Лютий» і т. д.

month =int(input('Оберить номер місяця який треба назвати (1-12)- '))
if month==1:
        print('"Січень"')
elif month==2:
        print('"Лютий"')
elif month==3:
        print('"Березень"')
elif month==4:
        print('"Квітень"')
elif month==5:
        print('"Травень"')
elif month==6:
        print('"Червень"')
elif month==7:
        print('"Лмпень"')
elif month==8:
        print('"Серпень"')
elif month==9:
        print('"Вересень"')
elif month==10:
        print('"Жовтень"')
elif month==11:
        print('"Листопад"')
elif month==12:
        print('"Грудень"')
else:
        print('Ви ввели не коректне значення.')


#Завдання 3
#Користувач вводить з клавіатури число. Якщо число більше
#0, виведіть напис «Number is positive», якщо менше 0 — «Number
#is negative», якщо дорівнює 0 — «Number is equal to zero».

try:
    zminna1 = float(input('ввдіть число: '))
    if zminna1 == 0 :
        print('Number is equal to zero')
    elif zminna1 > 0 :
        print('Number is positive')
    elif zminna1 < 0 :
        print('Number is negative')
except:
    print('Помилка!')

#Завдання 4
#Користувач вводить два числа. Визначте, чи рівні ці числа,
#якщо ні, виведіть іх на екран у порядку зростання.

try:
    zminna1 = float(input('введить перше число для порівняння'))
    zminna2 = float(input('введить друге число для порівняння'))
    if zminna1 == zminna2 :
        print('Ці числа рівні')
    elif zminna1 > zminna2 :
        print('Данні числа у порядку дростання:', zminna2,',',zminna1 )
    elif zminna2 > zminna1 :
        print( 'Данні числа у порядку дростання:' ,zminna1,',',zminna2 )
except:
    print('Помилка!')



