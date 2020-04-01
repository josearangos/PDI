# -*- coding: utf-8 -*-
"""
Created on 18 de marzo 2020

@author: Jose Alberto Arango Sánchez
"""

import cv2
import numpy as np
import time

paisaje = cv2.imread("paisaje.jpg")
carro = cv2.imread('carro.jpg')

[fil,col,cap]= carro.shape #Se obtienen las dimensiones del carro

paisaje_resize = cv2.resize(paisaje,(col,fil))# Se  cambia el tamaño de la imagen paisaje

"""
Realizamos el fundido normal, pero este se satura mucho
"""
carroPlusPaisaje =cv2.add(paisaje_resize,carro) #Sumar imagenes mediante openCV, con numpy img1+img2

cv2.imshow("CARRO + PAISAJE MUY SATURADO ",carroPlusPaisaje)

# Oculamos una imagen mientras la otra aparece, ejemplo del proyector
aux = paisaje_resize.copy()

for i in np.arange(0,1,0.01,float):
    g = cv2.addWeighted(paisaje_resize,1-i,carro,i,0)#Se funden las imagenes con diferentes pesos
    cv2.imshow('image',g)# Muestra la imagen
    time.sleep(0.01)#Tiempo de esperaentre la captura de cada frame
    cv2.waitKey(10)

cv2.waitKey(0)
cv2.destroyAllWindows()

















