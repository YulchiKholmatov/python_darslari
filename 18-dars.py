# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 07:40:14 2021

@author: Admin
"""
#18-dars WHILE YORDAMIDA RO'YXATNI TO'LDIRISH
ismlar = []
print("yaqin do'stlaringiz ro'yxatini tuzamiz")
n=1
while  True:
    savol= f"{n}-do'stingizni kiriting"
    ism=input(savol)
    ismlar.append(ism)
    javob = input("yana ism qo'shasizmi (ha/yo'q)")
    if javob == "ha":
        n+=1
        continue
    else:
        break
print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())
    
#
print("do'stlaringiz yoshini saqlaymiz")
dostlar={}
ishora = True
while ishora:
    ism=input("do'stingiz ismini kiriting")
    yosh = input(f"{ism.title()}ning yoshini kiriting")
    dostlar[ism]=int(yosh)
    javob = input("yana ma'lumot qo'shasizmi (ha/yo'q)")
    if javob =="yo'q":
        ishora=False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")


#
cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while "nexia" in cars:
    cars.remove('nexia')
print(cars)


#
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting")
    print(f"{talaba.title()} baholandi") 
    baholangan_talabalar[talaba]=baho
    
    

