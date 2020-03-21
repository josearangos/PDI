import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# PARTE 1 EXPLORACIÓN DE LA IMAGEN EN DIFERENTES MODELOS

# Con esta función normalizamos la imagen y la cambiamos de 3 a dos dimensiones
def chori(a):
    fil, col, cap = a.shape  # Extraemos sus dimensiones y las guardamos en variables separadas

    cv2.normalize(a, None, 0, 255, cv2.NORM_MINMAX)  # Normalizamos la imagen con Z-scored
    # Cambiamos las dimensiones de la imagen (de tres a dos dimensiones)
    # Order= f es para que nos muestre los ejes de las imagenes uno por uno en vez de uno por columna
    a = np.reshape(a, (fil, col * cap),order='f')
    return a

# Con esta función obtenemos las componentes de la imagen y las convertimos a diferentes formatos de imagen
def componentes(a,cmyk_image_resize):
    a1_chori = chori(a) #RGB
    """
    Modelo cordenadas HSV
    
    H-> angulo  equivalente R
    S-> saturacion  equivalente G
    I-> insentidas equivalente B
    
    """
    a2 = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)  # Tomamos la imagen en BGR y la convertimos a HSV

    a2_chori = chori(a2) #HSV

    a3 = cv2.cvtColor(a, cv2.COLOR_BGR2LAB)  # Tomamos la imagen en BGR y la convertimos a lAB
    a3_chori = chori(a3) #LAB

    return a,a2, a3,a1_chori,a2_chori,a3_chori # Retornamos las imagenes separadas por componentes en cada uno de los formatos


a = cv2.imread('carro.jpg', 1)  # Leemos la imagen a la cual le aplicaremos las dos funciones anteriores

#Dado que las componentes CMYK no estan por defecto en opecv, se procedera a usar la librería PIL
image = Image.open('carro.jpg')
#Convertimos la imagene de RGB a CMYK
cmyk_image = image.convert('CMYK')
#Convertimos de typo Image a numpyarray
cmyk_image = np.array(cmyk_image)

# Con esta y las tres lineas de codigo anteriores reducimos el tamaño de la imagen
# que leemos (Para nuestro caso específico era necesario pues no se mostraba en su totalidad )
a = cv2.resize(a, (700, 700),interpolation=cv2.INTER_AREA)


#Resize image CMYK
cmyk_image_resize = cv2.resize(cmyk_image[:,:,0:3], (700, 700),interpolation=cv2.INTER_AREA)


a,a2, a3,a1_chori,a2_chori,a3_chori= componentes(a,cmyk_image_resize)  # Aplicamos la función componentes que a su vez utiliza la función Chori
a4 = chori(cmyk_image_resize)


# Mostramos las imágenes
cv2.imshow('COMPONENTES RGB', a1_chori)
cv2.imshow('COMPONENTES HSV', a2_chori)
cv2.imshow('COMPONENTES LAB', a3_chori)
cv2.imshow('COMPONENTES CMYK', a4)



#-----------------------------------------------------------------------------------------------------------------

# PARTE 2 SACAR LA PLACA
"""
Luego de visualizar todas las imagenes, se nota a leguas que la placa se visualiza mejor en el formato CMYK en la componente 3
en el archivo selectLicensePlate.py se usara es mejor imagen para resaltar la placa
"""
#la mejor capa del formato del color por modelo
best_lab =a3[:,:,2]
best_hsv = a2[:,:,1]
best_cmyk = cmyk_image_resize[:,:,0]
#normalizamos las mejores capas por formato de color
cv2.normalize(best_lab, None, 0, 255, cv2.NORM_MINMAX)
cv2.normalize(best_hsv, None, 0, 255, cv2.NORM_MINMAX)
cv2.normalize(best_cmyk, None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow("MEJORES ",np.hstack([best_lab,best_hsv,best_cmyk]))

# Usamos el método de segmentación más simple.
ret, mask  = cv2.threshold(best_lab,0,255,cv2.THRESH_OTSU)
kernel = np.ones((5,3),np.uint8)
mask = cv2.erode(mask,kernel,iterations = 1)

cv2.imshow('PLACA BINARIZADA',mask)

#sacamos la placa de la imagen original
b2=cv2.resize(mask,(mask.shape[0],mask.shape[0]),interpolation=cv2.INTER_AREA)
cv2.normalize(b2, None, 0, 255, cv2.NORM_MINMAX)
a[b2==0]=0
cv2.imshow('ORIGINAL + PLACA',a)

cv2.waitKey(0)
cv2.destroyAllWindows()

