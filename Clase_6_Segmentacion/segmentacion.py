import numpy as np
import cv2
#parte 1 de la clase
a = cv2.imread('figuras.bmp',0) #Leemos una imagen
fil,col = a.shape # Extraemos su número de filas y columnas
ee = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) #Creamos un elemento estructurante (Una matriz de tamaño 5*5 que está dispuesta de manera rectangular)
cv2.imshow('figuras',a) #Mostramos la imagen que leímos
erosion = cv2.erode(a,ee,iterations = 15) #le aplicamos una erosión 15 veces con el elemento estrucurante que creamos antes
cv2.imshow('Erosion',erosion) #Mostramos la imagen erosionada
cv2.waitKey(0)
cv2.destroyAllWindows()

#Parte de 2 de la clase

b = cv2.imread('figuras_2.bmp',0) #Leemos una imagen
fil,col = b.shape # Extraemos su número de filas y columnas
cv2.imshow('figuras_2',b) #Mostramos la imagen
ee = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) #Usamos el mismo elemento estructurante que anteriormente
b = cv2.dilate(b,ee,iterations = 10) #Dilatamos 10 veces
b = cv2.erode(b,ee,iterations = 10) #Erosionamos 10 veces
cv2.imshow('Close_Figuras',b) #Mostramos la imagen en la cual lo que hicimos fue hacer close o cerrado (dilatar y luego erosionar)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Parte 2.1 de la clase

a = cv2.imread('figuras_2.bmp',0) #Leemos una imagen
b = cv2.morphologyEx(a,cv2.MORPH_OPEN,ee) #La aplicamos una apertura
cv2.imshow('close figuras_2',b) #la mostramos
c = cv2.morphologyEx(a,cv2.MORPH_CLOSE,ee) #Aplicamos un cierre a la imagen
cv2.imshow('pyClose_figuras2',c) #La mostramos
cv2.waitKey(0)
cv2.destroyAllWindows()

#Parte 3 de la clase

a = cv2.imread('figuras_2.bmp',0) #Leemos una imagen
ee = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) #Creamos nuestro elemento estructurante
b = cv2.erode(a,ee,iterations = 10) #le hacemos una erosión
c = np.subtract(a,b) #Restamos a la imagen original la erosonada
ab = np.concatenate((a,b)) #Creamos una donde estén juntas la original y la erosionada
#cv2.imshow('figuras_2',a)
#cv2.imshow('figuras_2_erode',b)
cv2.imshow('figuras-figuraserode',ab) #Mostramos la imagen original y la erosionada
cv2.imshow('resta_figuras-erode',c) #Mostramos la imagen que corresponde a la resta de las dos anteriores

cv2.waitKey(0)
cv2.destroyAllWindows()