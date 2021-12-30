# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 12:45:28 2021

@author: Admin
"""
#16-dars Nesting (konspekt)
car0={
      "model":"lacetti",
      "rang":"oq",
      "yil":2018,
      "narx":13000,
      "km":50000,
      "korobka":"avtomat"
      }
car1={
     "model":"nexia 3",
     "rang":"qora",
     "yil":2015,
     "narx":9000,
     "km":89000,
     "korobka":"mexanika"
     }
car2={
      "model":"gentra",
      "rang":"qizil",
      "yil":2019,
      "narx":15000,
      "km":20000,
      "korobka":"mehanika"
      }
cars=[car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()}, " 
          f"{car['rang']} rang, "
          f"{car['yil']} yil, {car['narx']}$")

print(cars[0]) #index bo'yicha print qilinmoqda
print(cars[0]['model']) #lug'tadagi birror elemntni chop qilish
print(cars[2]['model'])
print(cars[2]['rang'])


malibus=[]
for n in range(10):
    new_car ={
        "model":'malibu',
        "rang":None,
        "yil":2020,
        'narx': None,
        "km":0,
        "korobka":"avtomat"
        }
    malibus.append(new_car) 
    for malibu in malibus[:3]:
        malibu['rang']='qizil'
    for malibu in malibus[3:6]:
        malibu['rang']="qora"
        malibu['korobka']='mexanika'
    for malibu in malibus:
        if malibu['korobka']=="avtomat":
            malibu['narx']=40000
        else:
            malibu['narx']=35000
for malibu in malibus:
    print(malibu)
    
    
dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }
for ism,tillar in dasturchilar.items():
    print(f'\n {ism.title()} quyidagi dasturlash tillarini biladi')
    for til in tillar:
        print(til.upper())
        
for ism,tillar in dasturchilar.items(): 
    print(f"{ism.title()} quyidagi dasturlash tillarini biladi: ", end='')
    for til in tillar:
        print(f"{til.upper()} ", end='')
    
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }    
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())    
        
    
    

