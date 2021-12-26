# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 11:45:18 2021

@author: Admin
"""
cars = ["bmw", "mercedes benz", "volvo", "general motors", "audi"]
#cars.sort() #saralash
#cars.sort(reverse=True) # teskari saralash
print(cars)
print(sorted(cars))#ro'yxatga o'zgartirish kiritmasdan saralab konsolga chiqarish
print(sorted(cars, reverse=True))
cars.reverse() #teskarisiga chiqaradi
print(cars)
print(len(cars)) #ro'yxat uzunligi 
sonlar =list(range(0,10))
print(sonlar)
toq_sonlar = list(range(1,10,2))
print(toq_sonlar)
max_qiymat= max(toq_sonlar)
print(max_qiymat)
summa= sum(toq_sonlar)
print(summa)
print(cars[0:3])
mycars= cars[:]

#topshiriq

davlatlar= ["O'zbekiston", "AQSH", "Yaponiya", "Turkiya", "Misr"]
print(len(davlatlar))
print(sorted(davlatlar))            
print(sorted(davlatlar, reverse=True))
print(davlatlar)
print(davlatlar.reverse())
davlatlar.sort()
davlatlar.sort(reverse=True)
print(davlatlar)

sonlar= list(range(120,1201,2))
print(sonlar)
summa = sum(sonlar)
print(summa)
son_min = min(sonlar)
son_max = max(sonlar)
print(son_max-son_min)
print(len(sonlar))
print(sonlar[:20])
print(sonlar[530:550])
print(sonlar[-20:])

taomlar = ["osh", "manti", "sho'rva", "lag'mon", "somsa"]
nonushta = taomlar[:]
nonushta.remove("manti")
nonushta.remove("lag'mon")
nonushta.append("bo'tqa")
nonushta.append("tuxum")
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
print(type(nonushta))











