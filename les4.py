"""number = int(input('Введить число (до 10) - '))
while number < 10 :
    print('number =' ,number)
    number +=1
print('Цикл закінчився')"""
"""number = int(input('Введить число (до 10) - '))
while True:
    print('number =', number)
    number += 1
    if number >=10:
        break
    str = input('Бажаете продовжити - ')
    if str == 'no' or str == 'N':
        break"""

"""import random
#import random - библиотека ,
#можно так-
#from random import randint
#bot_number = randint(1,10)
print('Гра - Вгадай число')
bot_number = random.randint(1,10)
num_2 = 0
while True:
    num_2 += 1
    user_number = int(input('ВВедіть число до 10 - '))
    if  user_number > bot_number:

        print('Ваше число більше ніж у бота...')
    elif  user_number < bot_number:
        print('Ваше число меньше ніж у бота...')
    elif  user_number == bot_number:
        print('Ви вгадали число!')
        break

print('Гру закінчено...')
print(f'Вгадене число- {bot_number}...')
print(f'Ви вгадали за {num_2} спроби...')"""

"""number = input('Введить ціле число - ')
while type(number) != int:
    try:
        number =  int(number)

    except ValueError:
        print('Не вірно задане число...')
        number = input('Введить ціле число - ')
print('OK')"""

"""print('5+5**2=', eval('5+5**2')"""



"""x = 5
for i in 2,3,4:
    x += 1
    print(f'{i} --> {x}')
"""
"""x = 5
for i in range(5):
    x += 5
    print(f'{i} --> {x}')"""


"""for i in range(1,11):
    print('i - ', i)"""

"""number = input('Введить ціле число - ')
while type(number) != int:
    try:
        number =  int(number)

    except ValueError:
        print('Не вірно задане число...')
        number = input('Введить ціле число - ')
print('OK')
"""
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
        print('Ви ввели не коректне значення.')

