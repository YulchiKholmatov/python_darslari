# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:42:43 2021

@author: Admin
"""
a=20
b=5.5
print(type(a)) #type()orqali ma'lumot tipini bilish mumkin

aholi_soni=7_987_454_234 #uzun sonlarni _ bilan ajratib yozish
print(aholi_soni)

x, y, z = 10, 5.5, -56 # bir vaqtning o'zida ber nechta o'zgaruvchi

c=a*b
print(c)

radius = 20
PI = 3.14159
diametr= 2*radius 
print("aylana uzunligi =", PI*diametr) 
 
ism="jobir"
yosh=35
xabar= ism + " " + str(yosh) + " yoshda"
print(xabar)

t_yil=int(input("tug'ulgan yilingizni kiriting"))
yosh = 2021-t_yil
print("siz", yosh, "yoshda ekansiz")

#topshiriq
#1-topshiriq
son=int(input('istalgan sonni kiriting\n>>>'))
print(son, " ning kvadrati ", son**2, "ga teng", "\n", son,"ning kubi", son**3, "ga teng")

#2-topshiriq
yosh = int(input("yoshingiz nechada\n>>>"))
t_yil = 2021 - yosh 
print("siz", t_yil,"-yilda tug'ulgansiz")

#3-topshiriq
son1=int(input("birinchi sonni kiriting\n>>>"))
son2=int(input("ikkinchi sonni kiriting\n>>>"))
print(f"""{son1} + {son2} = {son1+son2} \n{son1} - {son2} = {son1-son2}
{son1} * {son2} = {son1*son2}\n{son1} / {son2} = {son1/son2}  """)





















