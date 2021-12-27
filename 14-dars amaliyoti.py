# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 09:47:06 2021

@author: Admin
"""
# 14-dars amaliyot 

otam = {"ism":"Abdujamil",
        "t_yil":1964,
        "t_joy":"Toshkent viloyati"}
print(f"Otamning ismi {otam['ism']} \
{otam['t_yil']}-yilda {otam['t_joy']}da tug'ulgan")

s_taomlar = {"otam":"osh",
             "onam":'mastava',
             "akam":'qozon kabob',
             "men":"qaynatma sho'rva",
             "jiyani":'shashlik'}
print(f"otamning sevimli taomi {s_taomlar['otam']}, \
onamning sevimli taomi {s_taomlar['onam']}, \
akamning sevimli taomi {s_taomlar['akam']}")


python_lugat= {"string":"matnli o'zgaruvchi turi",
               "int":"butun son ko'rinishidagi o'zgaruvchi turi",
               "float":"o'nlik son ko'rinishidagi o'zgaruvhi turi",
               "if":"(agar) shart operatori",
               "and":"(va) shart operatori",
               "or":"(yoki) shart operatori",
               "else":"(aks holda) shart operatori",
               "print":"chop qiluvchi metod",
               "**":"darajaga ko'tarish amali",
               "list":"ro'yxat o'zgaruvchi turi" }

lugat=input("iltiomos biror so'z kiriting")
#print(python_lugat.get(lugat, "bunday lug'at mavjud emas"))

if python_lugat.get(lugat):
    print(lugat, "bu", python_lugat.get(lugat),"dir" )
else: print("kechirashiz siz kiritgan so'z haqida hech qanday ma'lumot tompilmadi")
    


















