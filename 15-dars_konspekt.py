# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:05:21 2021

@author: Admin
"""

#15-dars Lug'at elementlari bilan ishlash. (konspekt)
talaba_0={"ism":"Aziz",
          "familya":"Abdullayev",
          "yosh":24,
          "kurs":1
        }
print(talaba_0.items()) #item yordamida chop qilish

for kalit,qiymat in talaba_0.items():
    print("kalit:", kalit)
    print('qiymat', qiymat)
    
    
telefonlar={
    "Ali":"ipxone x",
    'Vali': "galaxy s9",
    "Olim": "mi 10pro",
    "Orif": "nokia 3310"
    }
for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
    print(f"{k}ning telefoni: {q}")
    
    

    





    
    
    
    