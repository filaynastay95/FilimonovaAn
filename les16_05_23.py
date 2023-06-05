"""spysok=[2,4,7,12,34,1,56,78,9]
b=0
for i in spysok:
    b+=i

print(b)"""
"""
spysok=[2,4,7,12,34,1,56,78,9]
def calcSum(a):
    if a==[]:
        return 0
    else:
        summ=calcSum(a[1:])
        summ+=a[0]
        return summ
summ=calcSum(spysok)
print(summ)"""
"""
spysok=[2,-4,7,12,34,1,-56,78,-9]
def calcSumNegative(a):
    if a==[]:
        return 0
    else:
        count= calcSumNegative(a[1:])
        if a[0]<0:
            count+=1
        return count

n=calcSumNegative(spysok)
print(n)"""

"""
# Ряд Фібоначчі

def GetFibonacciList(n,l):
    count=len(l)
    if len(l)<2:
        return []

    num1=l[count-2]
    num2=l[count-1]

    if (num1+num2)<n:
        l=l+[num1+num2]
        return GetFibonacciList(n,l)
    else:
        return l

new = GetFibonacciList(100,[5,10])
print(new)"""

"""def Power(x,y):
    if y>0:
        return x*Power(x,y-1)
    else:
        return 1

x=3
y=4
resultat=Power(x,y)
print(resultat)"""


def calcSumPositive(a):
    if a==[]:
        return 0
    else:
        count= calcSumPositive(a[1:])
        if a[0]>0:
            count+=1
        return count

def GetMinList(l):
    if len(l)>1:
        Min = GetMinList(l[1:])
        if l[0]>Min:
            return Min
        else:
            return l[0]
    if len(l)==1:
        return l[0]




List=input('Ведить свый список через кому:').split(',')
List=[int(num) for num in List]
print(List)
VariantRaschet=int(input('Оберить що треба розрахувати: 1. кількість позитивних чисел у списку   2. Мінімальне значення чмсла  списку'))
if VariantRaschet ==1:
    positive = calcSumPositive(List)
    print(positive)
elif VariantRaschet ==2:
    mini =GetMinList(List)
    print(mini)
else:
    print('Невірно задане значення')
