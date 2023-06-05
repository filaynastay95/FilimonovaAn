"""zminna1 = ['A','B','C','D']
zminna2 = [1,2,3,4,]
# виводимо другий ел першого списка
print(zminna1[1])
#замін ост ел другого списка з 4 на 8
zminna2 [3]=8
print(zminna2)
#додали між собою два списка
zminna3= zminna1 +zminna2
print(zminna3)


import random

nums = []
for i in range(100):
nums.append(random.randint(-100, 100))

print(nums)"""


a=[-3,1,-1,5,6,8,-4,7,-5]
g= len(a)
x=0
while x < g:
    if a[x]>0:
        f=(a.index(a[x]))
        break
    x+=1
print(f)
x=-1
while x < g:
    if a[x]>0:
        p=(a.index(a[x]))
        break
    x-=1
print(p)
h= sum(a[f+1:p])
print(h)




