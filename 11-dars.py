# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:13:42 2021

@author: Admin
"""
yosh = int(input("yoshingiz nechada"))
if yosh<=4:
    narx=0
elif yosh<=12:
    narx=5000
else:
    narx=10000
print("siga kirish", narx ,"so'm")


kun = input("bugun qaysi kun")
if kun.lower()=="shanba" or kun.lower()=="yakshanba":
    print("bugun dam olish kuni")
else :
    print("bugun ish kuni")
    
    
    
    
menu=["osh","baliq","kabob","sho'rva","manti","lag'mon"]
ovqat=input("nima ovqat yeysiz")
if ovqat.lower() in menu:
    print("buyurtmangiz qabul qilindi")
else:
    print("Afsuski bizda bunday ovqat yo'q")
    
    
    #topshiriq
son= float(input("juft son kiriting"))
if son%2:
    print("bu son juft emas")
else : print("rahmat")


yosh = int(input("iltimos yoshingizni kiriting"))
if yosh<4 or yosh>60:
    narx = 0
elif yosh <18:
    narx=10000
else:
    narx=20000
print("siz uchun muzeyga kirish narxi", narx, "so'm")



print("iltimos ikkita son kirinting")
son1=int(input("1-sonni kiriting"))
son2=int(input("2-sonni kiriting"))
if son1==son2:
    qiymat="berilgan sonlar teng"
elif son1>son2:
    qiymat="1-son 2-sondan katta"
else: 
    qiymat="2-son 1-sondan katta"
print(qiymat)    
    


maxsulotlar = ["non", "olma", "tuz", "un", "yog'", "kitob", "daftar", "qlam", "anor", "uzum" ]
savat =[]
print("iltimos savatga kamida 5ta maxsulot kiriting")
for n in range(5):
    savat.append(input(f"{n+1}-maxsulotni kiriting "))
for maxsulot in savat:
    if maxsulot in maxsulotlar():
        print(f"{maxsulot} do'kinimizda bor")
    else:
        print(f"{maxsulot} do'kinimizda yo'q")
    
    
    
maxsulotlar = ["non", "olma", "tuz", "un", "yog'", "kitob", "daftar", "qlam", "anor", "uzum" ]
savat =[]
bor_maxsulotlar=[]
mavjud_emas=[]
print("iltimos savatga kamida 5ta maxsulot kiriting")
for n in range(5):
    savat.append(input(f"{n+1}-maxsulotni kiriting "))
for maxsulot in savat:
    if maxsulot in maxsulotlar:
        bor_maxsulotlar.append(maxsulot)
    else:
        mavjud_emas.append(maxsulot)
if mavjud_emas:
    print("quyidagi maxsulotlar do'konimizda yo'q:")
    print(mavjud_emas)
else:
    print("siz so'ragan barcha maxsulot do'konimizda bor")
    
    
    
foydalanuvchilar=["student", "teacher", "builder","user", "admin"]
login=input("login tanlang")

if login in foydalanuvchilar:
    print("login band yangi login tanlang")
else : 
    print("xush kelibsiz")
    
    
son = int(input("biror butun son kiriting"))
for n in range(2,11):
    if not son%n:
        print(n)    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    