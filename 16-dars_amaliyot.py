# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 08:03:26 2021

@author: Admin
"""
#16-dars amaliyot
#Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar 
#haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni 
#bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni 
#konsolga chiqaring.
buxoriy={
    "ism":"Abu Abdulloh Muhammad ibn Ismoil ibn Ibrohim al Buxoriy ",
    "t_yil":810,
    "t_joy":"Buxoro",
    "asarlari":["«Al-jome’ as-sahih»","«Al-adab al-mufrad»", "«At-tarix al-kabir»"]
    }
gazzoliy={
    "ism":"Abu Homid Muhammad ibn Muhammad al-Gʻazzoliy ",
    "t_yil":1058,
    "t_joy":"Tus (Eron)",
    "asarlari":["Ihya ulum ad-din","Mukoshafat ul-qulub", "Qavoid al-Aqoid"]
    }
beruniy={
    "ism":"Abu Rayhon Beruniy Muhammad ibn Ahmad",
    "t_yil":973,
    "t_joy":"Xorazm",
    "asarlari":["Hindiston", "Yodgorliklar", "Qonuni Masʼudiy", "Geodeziya", "Astronomiya"]
    }
shayx={
       "ism":"Shayx Muhammad Sodiq Muhammad Yusuf ibn Muhammad Ali",
       "t_yil":1952,
       "t_joy":"Andijon viloyati",
       "asarlari":["Iymon","Baxtiyor oila","Hadis va hayot"]
       }
olimlar=[buxoriy,gazzoliy,beruniy,shayx]
for shaxs in olimlar:
    print(f'{shaxs["ism"]} {shaxs["t_yil"]}-yilda {shaxs["t_joy"]}da tug\'ulgan')

#Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini
#ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini
#konsolga chiqaring.
for ism_asar in olimlar:
    print(f"{ism_asar['ism']}ning mashhur asarlari {ism_asar['asarlari']}")
    
#Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar 
#haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida 
#ma'lumotni konsolga chiqaring.

davlatlar={
    "O'zbekiston":{
        "poytaxti":"Toshkent",
        "aholi_soni":"35 mlndan ortiq",
        "d_tili":"o'zbek"
        },
    "AQSH":{
        "poytaxti":"Vashington",
        "aholi_soni":"320 mlndan ortiq",
        "d_tili":"ingliz"
        },
    "Rossiya":{
        "poytaxti":"Moskva",
        "aholi_soni":"146 mlndan ortiq",
        "d_tili":"rus"
        }
    }
savol=input("biror davlar nomini kiriting")
print(davlatlar.get(savol,"bizda bunday davlat haqida ma'lumot yo'q"))    










