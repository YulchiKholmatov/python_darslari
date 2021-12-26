# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:26:41 2021

@author: Admin
"""
avtolar=["audi", "bmw", "volvo", "kia", "hyundai"]
for avto in avtolar:
    if avto=="bmw":
        print(avto.upper())
    else:    
        print(avto.title())

a=5

ism=input('ismingizni kiriting\n<<<<')
if ism.lower() != "ali":
    print(f"uzur {ism.title()} biz Alini kutyapmiz")
else:
    print("salom Ali")

yosh=int(input("yoshingiz nechada"))
if yosh>=18:
    print("xush kelibsiz")
else:
    print("kirish mumkin emas")

login=input("yangi login tanlang")
if len(login)<5:
    print("login 5ta belgidan ko'proq bo'lishi kerak")

#topshiriq
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car=="gm":
        print(car.upper())
    else:
        print(car.title())
        
        
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car!="gm":
          print(car.title())
    else:
          print(car.upper())
          
          
user_name=input("ismingizni kiriting")
if user_name.lower()=='admin':
    print("Xush kelibsiz admin! Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"{user_name.title()}!aa")


print("2ta son kiriting")
son1=int(input("1-sonni kiriting"))
son2=int(input("2-sonni kiriting"))
if son1==son2:
    print('sonlar teng ekan')
    
    

son=int(input("istalgan sonni kirting"))
if son>0:
    print("Musbat son")
else:
    print("manfiy son")
    
    
    
son=float(input("son kiriting"))
if son>0:
    print(son**0.5)
else:
    print("musbat son kiriting")
      


































    





