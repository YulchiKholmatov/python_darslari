# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:19:39 2021

@author: Admin
"""

#15-dars While (konspekt)

son = 1
while son <=5:
    print(son, end = ' ')
    son=son+1  #yoki son+=1
print("dastur tugadi")


print('kritilgan sonning kvadratini hisoblovchi dastur')
savol = "istalgan sonni kiriting"
savol += "dasturni tugatish uchun 'exit' deb yozing"
qiymat = ''
while qiymat != 'exit':
    qiymat =input(savol)
    if qiymat != "exit":
        print(float(qiymat)**2)
print("dastur tugadi")


ishora = True
print('kritilgan sonning kvadratini hisoblovchi dastur')
savol = "istalgan sonni kiriting"
savol += "dasturni tugatish uchun 'exit' deb yozing"
qiymat = ''
while ishora:
    qiymat =input(savol)
    if qiymat == "exit":
        ishora=False
    else:
        print(float(qiymat)**2)
print("dastur tugadi")



print('kritilgan sonning kvadratini hisoblovchi dastur')
savol = "istalgan sonni kiriting"
savol += "dasturni tugatish uchun 'exit' deb yozing"
qiymat = ''
while True:
    qiymat =input(savol)
    if qiymat == "exit":
        break
    else:
        print(float(qiymat)**2)
print("dastur tugadi")



sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
    print(son,"ning kvadrati", son**2, "ga teng" )



sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue
    print(son,"ning kvadrati", son**2, "ga teng" )


son = 0
while son<10:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)




















    