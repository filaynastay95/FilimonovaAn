"""student = ['Bob',19,95]
template= "Name:{}: age:{}; score{}"
user=['admin','teacher','manager']

while True:
    user = input('Login')
    print('1-print info')
    print('2-modify info')
    print('3-exit')
    userChoice= input('Select menu item: ')
    if userChoice =='1':
        user= input('Login')
        if user in users:
            print('Current information:')
            print(template.format(student[0],
                                  student[1],
                                  student[2],))
    elif userChoice =='2':
        user = input('Login')
        if user in users:
            print('Current information:')
            print(template.format(student[0],
                                  student[1],
                                  student[2], ))
            userAnsw=input('Change this info y-n')
            if userAnsw=='y':
                name=input('Inpu new name')
                age= input('Age')
                score=input('score')
                student[0]=name
                student[1]=age
                student[2]=score
                print(template.format(student[0],
                                      student[1],
                                      student[2], ))
        elif userChoice=='3':
            print('bay')
            break
        else:
            print('Error')"""
import math
"""a=0.23
b=1.87
c=3
print(math.ceil(a))
print(math.ceil(b))
print(math.ceil(c))

print(math.floor(a))
print(math.floor(b))
print(math.floor(c))"""

#modf()- овертае дробову част та цілу част числа
"""x=2.45
y=1.5
print(math.modf(x))
print(math.modf(y))"""

#trunc() - отримання цілої частини числа
"""x=2.45
y=1.5
print(math.trunc(x))
print(math.trunc(y))"""

#abs -повертає модуль числа (-2 = 2) з таким самим типом як і вихідне число
#fabs - повертае модуль числа с типом float
"""a=-2
b=-2.5
c=4
print(math.fabs(a))
print(math.fabs(b))
print(math.fabs(c))

print(abs(a))
print(abs(b))
print(abs(c))"""

#factorial - факториал 4!=4*3*2*1=24 всегда если число не целое =Value error
#або TypeError
"""try:
    a = 4
    b = 7.4
    print(math.factorial(a))
    print(math.factorial(b))
except TypeError:
    print('not correct item')"""

import random
#randint(a,b)- ринимает два аргумента и с єтого диапазона вібирет рандомное число
#первій аргкмент всегда меньше ворого
#randrange()- от одного до трех агрументов
#randrange(a) рандомное число от 0 до а[0:a] от нля до а-1
#randrange(a,b) от a до b-1  [a;b]
#randrange(a,b,c) первие два числа граници рандома с- шаг диапазона

"""
import random
for i in range(3):
    print('step',i+1)
    print(random.randint(1,5))
    print(random.randint(-3, 20))
    print(random.randint(-10, -6))"""

"""import random
for i in range(3):
    print('step',i+1)
    print(random.randrange(10))
    print(random.randrange(-3, 3))
    print(random.randrange(10,20,3))#10 13 16 19"""

#random  виклик без аргументів, випадкове числ генерується в діапаз від 0 до 1
"""import random
for i in range(3):
    print('step',i+1)
    print(random.random())"""

#choice(l) - l-це послідовність або її ім'я ф-ція для отримання випад ел з послідовності"""
"""import random
L=[1,24,'bob',True,False,7.9,'hello']
for i in range(3):
    print(random.choice)"""
"""import random
peremenna= float(input('ведить число'))
vvod=input('Введить що треба розрахувати')
if vvod =='факторіал':
    print(math.factorial(peremenna))
elif vvod =='абсолютне значення':
    print(abs(peremenna))
elif vvod =='згенерувати ':
    print(random.randint(1,10))
elif vvod =='згенерувати число в диапазоні':
    a=int(input('задайте початок діапазону'))
    b = int(input('задайте кінець диапазону'))
    print(random.randrange(a,b))
elif vvod =='ціла та дробова частина':
    print('дробова частина',math.modf(peremenna))
    print('ціла частина',math.trunc(peremenna))"""

"""def printMsg():
    print('hello')
    print('welcome')
printMsg()"""



#Завдання 1
#Створіть програму, що містить інформацію про відомих
#баскетболістів. Збережіть ПІБ та зріст кожного баскетболіста. Реалізуйте можливість додавати, видаляти, знаходити та
#змінювати дані. Використовуйте словник для збереження
#інформації


players={'Алексейчик':{'ПІБ':{'Призвище':'Алексейчик',"Ім'я":'Ольга'},'Зріст':'165'},
        'Балабан':{'ПІБ':{'Призвище':'Балабан',"Ім'я":'Вікторія'},'Зріст':'175'},
        'Волошина':{'ПІБ':{'Призвище':'Волошина',"Ім'я":'Владислава'},'Зріст':'178'},
        'Гаврильчик':{'ПІБ':{'Призвище':'Гаврильчик',"Ім'я":'Тетяна'},'Зріст':'194'}}
while True:
    vibor_rab_ili_net=input('Бажаєте продовжити работу:Так/Ні')
    if vibor_rab_ili_net=='Так':
        funkciia_sho_robumo = input('''Оберить, що треба реалізувати:
            додати інформацію про нового ігрока - 1
            видалити інформацію про ігрока - 2
            скерегувати данні по іграку - 3
            пошук інформації по іграку - 4
            вивести всф данні - 5\n''')
        if funkciia_sho_robumo == '1':
            last_name = input('Призвище ігрока:')
            name = input("Ім'я ігрока")
            height = input('Зріст ігрока')
            players[last_name] = {'ПІБ': {'Призвище': last_name, 'Ім`я': name}, 'Зріст': height}
        elif funkciia_sho_robumo == '2':
            delete_player = input('Введить призвище ігрока')
            del players[delete_player]
            print(players)
        elif funkciia_sho_robumo == '3':
            key_last_name = input('Введить призвище ігрока')
            type_info = input('Введить тип інформації, яку керегуємо')
            if type_info == 'Призвище':
                new_last_name = input('Нове призвище ігрока:')
                players[key_last_name]['ПІБ'][type_info] = new_last_name
            elif type_info == "Ім'я":
                new_name = input("Нове ім'я ігрока")
                players[key_last_name]['ПІБ'][type_info] = new_name
            elif type_info == 'Зріст':
                new_height = input('Новий зріст ігрока')
                players[key_last_name][type_info] = new_height
        elif funkciia_sho_robumo == '4':
            type_info = input("Введить тип інформації за якою проводимо пошук(Призвище/Ім'я/Зріст)")
            danni_poshyky = input('Введить данні')
            if type_info == 'Зріст':
                for player in players:
                    if players[player].get(type_info) == danni_poshyky:
                        print(players[player])
                        break
            if type_info == 'Призвище':
                print(players.get(danni_poshyky))
            if type_info == "Ім'я":
                for player in players:
                    if players[player]['ПІБ'].get(type_info) == danni_poshyky:
                        print(players[player])
                        break
        elif funkciia_sho_robumo == '5':
            print(players)
    if vibor_rab_ili_net == 'Ні':
        print('До зустрічі!')
        break
















