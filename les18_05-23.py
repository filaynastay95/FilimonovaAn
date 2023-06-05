"""f1=open('D:\\python1\\files\\myfiles1.txt','r')
s1=f1.readline() # прочитать строку одна
print(s1)
s2=f1.readline()
print(s2)"""

"""f1=open('D:\\python1\\files\\myfiles1.txt','r')
#print(f1.read()) # читання з файлу , працює тільки один раз
print(f1.read(5))
print(f1.read())"""

"""f1=open('D:\\python1\\files\\myfiles1.txt','r')
lines=f1.readlines() #читати файл у список рядків
print(lines)"""
"""
f1=open('D:\\python1\\files\\myfiles1.txt','r')
for line in f1:
    print(line)"""
"""
import random
i=0
spysok =[]
while i<10:
    chislo=random.randint(0,1001)
    spysok+=[chislo]
    i+=1
print(spysok)
f=open('D:\\python1\\files\\spysok.txt','w')
s=str(len(spysok))
f.write(s+'\n')
for i in spysok:
    s=str(i)
    f.write(s+' ')
f.close()"""
"""
f=open('D:\\python1\\files\\spysok.txt','r')
lines=f.readlines()
print(lines)"""

"""spysok_txt=['asd','asdfg','qwerty','zxcvbn','hjklo']
f=open('D:\\python1\\files\\spysok_strok.txt','w')

for line in spysok_txt:
    f.write(line+'\n')
f.close()"""

"""
slovnyk={1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri'}
f=open('D:\\python1\\files\\slovnyk.txt','w')
for item in slovnyk:
    s= str(item)
    s+=':'
    s+=slovnyk.get(item)
    s+='\n'
    f.write(s)

f.close()
"""
"""
f1=open('D:\\python1\\files\\myfiles1.txt','r')
count=0
s=f1.readline()
while s!='':
    s=f1.readline()
    count+=1
print(count)"""
"""
f2=open('D:\\python1\\files\\myfiles1.txt','r')
spysok=f2.readlines()
count=len(spysok)
print(count)"""

"""f3=open('D:\\python1\\files\\python.txt','r')
s=input('Enter text for change: ')
pos=2
spysok=f3.readlines()
if (pos>=0) and (pos<len(spysok)):
    if (pos==len(spysok)-1):
        spysok[pos]=s
    else:
        spysok[pos] = s+'\n'
f3.close()
f3=open('D:\\python1\\files\\python.txt','w')
for line in spysok:
    f3.write(line)
f3.close()"""

"""pos= int(input('pos='))
f=open('D:\\python1\\files\\python.txt','r')
spysok=f.readlines()
if (pos>=0) and (pos<len(spysok)):
    i=pos
    while i<len(spysok)-1:
        spysok[i]=spysok[i+1]
        i+=1
    spysok=spysok[:-1]
f.close()
f=open('D:\\python1\\files\\python.txt','w')
for line in spysok:
    f.write(line)
f.close()"""

"""f1=open('D:\\python1\\files\\myfiles1.txt','r')
f2=open('D:\\python1\\files\\myfiles2.txt','r')

spysok1=f1.readlines()
spysok2=f2.readlines()
spysok3=spysok1+['\n']+spysok2

f1.close()
f2.close()

f3=open('D:\\python1\\files\\union.txt','w')
for i in spysok3:
    f3.write(i)
f3.close()"""



