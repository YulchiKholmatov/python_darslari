# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 08:20:00 2021

@author: Admin
"""
#18-dars amaliyot
#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar 
#nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
buyurtmalar=[]
print("buyurtmangizni kiriting")
n=1
while True:
    savol=f"{n}-buyurtmangizni kiriting"
    buyurtma=input(savol)
    buyurtmalar.append(buyurtma)
    javob=input("buyurtma qoldirishni davom ettirasizmi (ha/yo'q")
    if javob == "ha":
        n+=1
    else:
        break
print("qabul qilingan buyurtmalar")
for buyurtma in buyurtmalar:
    print(buyurtma.title())
    

#e-bozor uchun mahsulotlar va ularning narhlari lug'atini 
#shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga 
#bir nechta elementlar (mahsulot va uning narhi) kiritishni
# so'rang.

maxsulotlar={}
while True:
    maxsulot=input("maxsulot nomini kiriting")
    narx=input(f"{maxsulot} narxini kiriting")
    maxsulotlar[maxsulot]=narx
    savol=input("maxsulot kiritishni davom ettirasizmi (ha/yo'q)")
    if savol!="ha":
        break
print(maxsulotlar)
    
#Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi 
#ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar 
#bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
#Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
#aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in maxsulotlar.keys():
        narh = maxsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
       
    
    
    
    
    
    
    