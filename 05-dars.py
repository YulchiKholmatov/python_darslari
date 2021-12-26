# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 08:27:22 2021

@author: Admin
""" ism="Ahmad"
print("mening ismim " + ism)
ism1="Ahad"
familya="Qayum"
print(ism + " " + familya)
ism_familya=f"{ism} {familya}"
print(ism_familya)

ism2='james'
familya2='Bond'
print(f"Salom mening ismim {ism2}. {ism2} {familya2}")

#Maxsus belgilar
print("hello world")
print("hello \tworld") # \t uzun boshliq qoldiradi

#string methodlar
print(ism_familya.upper()) #matnning barcha harflarini katta harf qilish uchun
print(ism_familya.lower()) #kichik harfga
print(ism_familya.title()) #so'z bosh harfi katta
print(ism_familya.capitalize()) #faqat matnning 1-harfi katta

olma='     olma         '
print(olma)
print(olma.lstrip()) #chap tomondagi boshliqni olib tashlash uchun
print(olma.rstrip()) #o'ng tomondagi bo'shliqni olib tashlash uchun
print(olma.strip()) #ikki tomondagi bo'shliqlarni olish uchun

#input
ism3=input("ismingiz nima")
print("Assalomu alaykum " + ism3) ###

#  topshiriq
#1-topshiriq
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

#2-topshiriq
kocha=input("Ko'changiz?\n>>>>")
mahalla=input("mahallangiz?\n>>>")
tuman=input("tumaningiz?\n>>>>")
viloyat=input("viloyatingiz?\n>>>")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")






































