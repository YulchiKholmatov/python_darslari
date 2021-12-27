# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 10:26:42 2021

@author: Admin
"""

car_0 ={"model":"ferari", "rang":"qizil"}
#print(car_0["model"])
#print(car_0["rang"])

mevalar= {"olma":10000, "tarvus":8000, "qovun":10000}
#print(f"olmaning narxi {mevalar['olma']} so'm")

talaba_0 = {"ism":"Dilshod", "yosh":24, "t_yil": 1997}
#print(f"{talaba_0['ism'].title()}, {talaba_0['t_yil']}-yilda tug'ulgan \
#{talaba_0['yosh']}  yoshda")

talaba_0['kurs']=4
talaba_0['fakultet']="xususiy huquq" # lug'atga yangi kalit va qiymat qo'shish
talaba_0['ism']="Abdulloh"  #qiymatni o'zgartirish

del talaba_0['yosh'] # elementni o'chirish
#print(talaba_0)

meva=mevalar.get("shaftoli","Bunday meva mavjud emas") # kalit mavjud bo'lmasa ushbu ma'lumot chiqadi
#print(meva)
