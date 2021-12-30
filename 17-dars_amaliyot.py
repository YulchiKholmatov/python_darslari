# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:46:47 2021

@author: Admin
"""

#17-dars amaliyot

#1-topshiriq
#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni 
#so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni 
#to'xtating

kitoblar="yaxshi ko'rgan kitoblazingizni kiriting"
kitoblar+='dastur to\'xtashi uchun stop deb yozing' 
qiymat=''
while qiymat!='stop':
    qiymat=input(kitoblar)
    if qiymat != 'stop':
        print(qiymat)
print('dastur tugadi')    


#2-topshiriq
#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga
 #- 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan 
 #kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi 
 #yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki 
 #quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
 
savol="yoshingizni kiriting"
savol+="dasturni to'xtatish uchun exit yoki quiet deb yozing"
qiymat=''
while qiymat != ('exit' or "quiet"):
    qiymat=input(savol)
    if qiymat=='exit' or qiymat=='quiet':
        break
    qiymat1=int(qiymat)
    if   qiymat1<7 :
        narx=2000
    elif qiymat1>6 and qiymat1<18 :
        narx=3000
    elif qiymat1>17 and qiymat1<65 :
        narx=10000    
    else:
        narx=0
    print("siz uchun chipta narxi",narx, "so'm")
print('dastur tugadi')



    







