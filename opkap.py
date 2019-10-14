b1=200
b2=100
r=10

import math
from math import cos
from math import sin
import numpy as np
t1=90
t2=90+120
t3=t2+120

#преобразование угла из градусов в радианы
def preobr(k):
    return (k*math.pi/180)

#вычисление координат перуна
perun11=r*cos(preobr(t1))
perun12=r*sin(preobr(t1))
perun21=r*cos(preobr(t2))
perun22=r*sin(preobr(t2))
perun31=r*cos(preobr(t3))
perun32=r*sin(preobr(t3))
d=24 #угол поворота в градусах посолонь




vniz_vlevo = np.array([[1,0,0], [-b1,1,0], [-b2,0,1]])
vniz_vpravo = np.array([[1,0,0], [b1,1,0], [-b2,0,1]])
vverch_vlevo = np.array([[1,0,0], [-b1,1,0], [b2,0,1]])
vverch_pravo = np.array([[1,0,0], [b1,1,0], [b2,0,1]])

def vrashenie(x,ve):
    arr=np.array([[1,0,0], [0,cos(preobr(x)),-sin(preobr(x))], [0,sin(preobr(x)),cos(preobr(x))]])
    ve1=ve.transpose()
    m = np.dot(arr, ve1)
    return m


def vniz_vlevo1(x1,x2,ve):
    arr = np.array([[1,0,0], [-x1,1,0], [-x2,0,1]])
    ve1 = ve.transpose()
    m = np.dot(arr, ve1)
    return m


def vniz_vpravo(x1,x2,ve):
    arr = np.array([[1,0,0], [x1,1,0], [-x2,0,1]])
    ve1 = ve.transpose()
    m = np.dot(arr, ve1)
    return m

def  vverch_vlevo(x1,x2,ve):
    arr = np.array([[1,0,0], [-x1,1,0], [x2,0,1]])
    ve1 = ve.transpose()
    m = np.dot(arr, ve1)
    return m

def vverch_pravo(x1,x2,ve):
    arr = np.array([[1,0,0], [x1,1,0], [x2,0,1]])
    ve1 = ve.transpose()
    m = np.dot(arr, ve1)
    return m

print("perun11 ",perun11)
print("perun12", perun12)
per1 = np.array([1,perun11, perun12])
print("per1 ", per1)

per2 =np.array([1,perun21, perun22])
print("per2 ", per2)

per3 =np.array([1,perun31, perun32])
print("per3", per3)


dper1=vrashenie(d,per1)
print("dper1 ", dper1)
ddper1=vverch_pravo(200, 100, dper1)
#ddper1=
print("ddper1 ", ddper1) #" ", int(ddper1[0,0]+ddper1[0,1]+ddper1[0,2]), " ", int(ddper1[1,0]+ddper1[1,1]+ ddper1[1,2]), " ", int(ddper1[2,0]+ddper1[2,1]+ ddper1[2,2]))


dper2=vrashenie(d,per2)
ddper2=vverch_pravo(200,100,dper2)
print("ddper2 ", ddper2)# " ", int(ddper2[0,0]+ddper2[0,1]+ddper2[0,2]), " ", int(ddper2[1,0]+ddper2[1,1]+ ddper2[1,2]), " ", int(ddper2[2,0]+ddper2[2,1]+ ddper2[2,2]))

dper3=vrashenie(d,per3)
ddper3=vverch_pravo(200,100,dper3)
print("ddper3 ", ddper3)#" ", int(ddper3[0,0]+ddper3[0,1]+ddper3[0,2]), " ", int(ddper3[1,0]+ddper3[1,1]+ ddper3[1,2]), " ", int(ddper3[2,0]+ddper3[2,1]+ ddper3[2,2]))
#  все идет путем!

#проверка пусть будет там
#поработаем над сварогом

#не поработала :X





#lost=[[1, 0, 0], [-b1+b1*math.cos(teta)-b2*math.sin(teta), math.cos(teta), -math.sin(teta)], [b2+b2*math.cos(teta)-b1*math.sin(teta), math.sin(teta), math.cos(teta)]]

#правка на 10 марта 2019 года
#Svarog
#-300,-125 -315,-110 -315,-140 -330,-125 , координаты его идолищ
svarog11=-300
svarog12=-125
svarog1=np.array([1,svarog11,svarog12])
svarog21=-315
svarog22=-110
svarog2=np.array([1,svarog21,svarog22])
svarog31=-315
svarog32=-140
svarog3=np.array([1,svarog31,svarog32])
svarog41=-330
svarog42=-125
svarog4=np.array([1,svarog41,svarog42])

svarog_centr1=-315
svarog_centr2=-125

#cначала операторы направо на 315 вверх на 125
#потом поворот противосолонь
# чтобы они оказались в 10 саженях от центра капища - то есть сжать или растянуть, то есть сжать, был радиус 15, должен стать 10
ds=-118 # протвосолонь на 118 градусов поворот совершить

dsv1=vverch_pravo(315,125,svarog1)
dsv2=vverch_pravo(315,125,svarog2)
dsv3=vverch_pravo(315,125,svarog3)
dsv4=vverch_pravo(315,125,svarog4)
print(dsv1)
print(dsv2)
print(dsv3)
print(dsv4)

ddsv1=vrashenie(ds,dsv1)
ddsv2=vrashenie(ds,dsv2)
ddsv3=vrashenie(ds,dsv3)
ddsv4=vrashenie(ds,dsv4)

print(ddsv1)
print(ddsv2)
print(ddsv3)
print(ddsv4)

#осталось сделать сжатие
