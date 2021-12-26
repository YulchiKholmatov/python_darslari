# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:37:43 2021

@author: Admin
"""
mevalar = ["olma", "anjir", "shaftoli", "o'rik"]
narxlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
sonlar = ["bir", "ikki", 3, 4, 5]
ismlar = []

mevalar[0]="anor"
mevalar[-1]="uzum"
mevalar.append("o'rik") # ro'yxat oxiriga obyekt qo'shish
mevalar.insert(0, "banan") # ro'yxat indexi bo'yicha obyekt qo'shish
del mevalar[1] # ro'yxatdagi obyektni indexi bo'yicha o'chirish
mevalar.remove("shaftoli") # qiymat orqali o'chirish
meva=mevalar.pop(0) #ro'yxatdan sug'urib olish
meva1=mevalar.pop() #ro'yxatdan oxirgi elementni sug'urib oladi
print(mevalar)

#topshiriq
ismlar=["Aziz", "Dilshod", "Temurbek"]
print(f"""Salom {ismlar[0]} bugun choyxona bormi
 {ismlar[1]} choyxonaga boramizmi """)
