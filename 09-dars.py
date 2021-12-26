# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:39:47 2021

@author: Admin
"""

mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
for mehmon in mehmonlar:
    print("salom", mehmon)

sonlar =list(range(1,10))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

sonlar1 = list(range(11))
sonlarkvadrati=[]
for son in sonlar1:
    sonlarkvadrati.append(son**2)
    
print(sonlar1)
print(sonlarkvadrati)

dostlar=[]
print("5 ta eng yaqin do'stingizni kiriting")
for n in range(5):
    dostlar.append(input( f"{n+1}-do'stingiz ismini kiriting"))
print(dostlar)

#topshiriq
ismlar=["Ali", "Vali", "Olim", "Nozim", "Temur"]
for ism in ismlar:
    print("Assalomu alykum", ism, "Hush kelibsiz")
print("kod", len(ismlar), "martta takrorlandi")

toq_sonlar = list(range(11,110,2))
print(toq_sonlar)
for son in toq_sonlar:
    print(son**3)

kinolar=[]
print("Iltimos 5ta eng sevimli kinolaringizni kiriting")
for n in range(5):
    kinolar.append(input((f"{n+1}-kinoni kiriting")))
print(kinolar)
     
