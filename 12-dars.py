# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:57:35 2021

@author: Admin
"""
#topshiriq

son = float(input("Juft son kiriting: "))
if son%2!=0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")
    
    
yosh = int(input("Yoshingiz nechida?"))
if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")