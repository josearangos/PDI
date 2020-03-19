# -*- coding: utf-8 -*-
import cv2
import numpy as np  


def mouse(event, x, y, flags, param): #Método  encargdo de devolver el valor del pixel en la imagen
    color=(255,2555,255)  #Se  asigna un color al texto que vamos a mostrar con la información del pixel
    posicion=(20,380) #De igual manera se le asigna una posición
    a=imagen.copy()  #Debido a que mostraremos la información del pixel en la imaen, creamos una copia para no alterar la original
    if event==cv2.EVENT_MOUSEMOVE: #Evento que se llama cada  vez que se mueve el mouse
        texto=imagen.item(y, x, 2), imagen.item(y, x, 1), imagen.item(y, x, 0) #Asignamos a texto los tres valores que componen el pixel
        cv2.putText(a,str(texto), posicion,1, cv2.FONT_HERSHEY_DUPLEX, color)#Hacemos uso del método de OpenCV ue permite poner texto en imagenes, al que le  mandamos respectivamente la imagen, el texto a poner en formato String, la  posición, tipo de fuente y color.
        
        cv2.imshow('image', a)#Se muestra la imagen (copia) en la cual se escribe la información de la matriz
        
        #cv2.putText(imagen,"", posicion,1, cv2.FONT_HERSHEY_DUPLEX, color)
        
def separar(imagen):
    while(1):
        cv2.namedWindow('image')#Se crea la ventana con la imagen a mostrar
        
        #[fil,col,cap]=imagen.shape
        a=imagen
        cv2.imshow('image',imagen)# Muestra la imagen
        cv2.setMouseCallback('image',mouse)#Se llama al método encargado de decirnos la posicion del mouse cada que se mueva y la información de la mat4riz en esa posición
        k = cv2.waitKey(0)
        if k == ord('s'):#Esperar hasta que se presione 's'
            break
    cv2.destroyAllWindows()#Se cierran las ventanas

if __name__=='__main__':
  imagen = cv2.imread("carro_test_impixel_info.jpg")#Se lee la imagen


  imagen=cv2.resize(imagen,(400,400))# Se cambia el tamaño de la imagen para poder apreciar la información
 
 #Se llama al método encargado de separar la imagen
  separar(imagen)

