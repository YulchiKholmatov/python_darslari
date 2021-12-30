# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:57:59 2021

@author: Admin
"""
#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z 
#qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli 
#yordamida, alifbo ketma-ketligida chiroyli qilib konsolga
 #chiqaring.
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
for k,q in sorted(python_lugat.items()):
    print(f"{k} - {q}dir")
    
    
#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval 
#lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, 
#alifbo ketma-ketligida konsolga chiqaring.
poytaxtlar={
    "O'zbekiston":"Toshkent",
    "AQSH":"Vashington",
    "Rossiya":"Moskva",
    "Koreya":"Seul",
    "Yaponiya":"Tokio"
    }
for d in sorted(poytaxtlar):
    print(d)
for p in sorted(poytaxtlar.values()):
    print(p)    
    
    
    
#Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu 
#davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi 
#lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q"
 #degan xabarni chiqaring.
poytaxtlar={
    "O'zbekiston":"Toshkent",
    "AQSH":"Vashington",
    "Rossiya":"Moskva",
    "Koreya":"Seul",
    "Yaponiya":"Tokio"
    }
savol=input("biror bir davlat nomini kiriting")
poytaxt=''
a=True
for d,p in poytaxtlar.items():
    if d.lower()==savol.lower():
        a=False
        print(f"{savol}ning poytaxti {p}")
if a == True:
    print("bunday ma'lumot mavjud emas")
      

#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh
#juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma 
#berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan 
#solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
#aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu={
     "osh":15000,
     'somsa':5000,
     "shashlik":9000,
     "sho'rva":12000,
     "lag'mon":14000,
     "manti":12000,
     "baliq":17000,
     "sharbat":4000,
     "choy":2000,
     "non":3000
     }
print("uchta toam kiriting")
buyurtma_1=input("1-taomni kiriting")
buyurtma_2=input('2-taomni kiriting')
buyurtma_3=input('2-taomni kiriting')
print(menu.get(buyurtma_1,"bunday taom yo'q"))
print(menu.get(buyurtma_2,"bunday taom yo'q"))
print(menu.get(buyurtma_3,"bunday taom yo'q"))
































































