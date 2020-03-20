import cv2
import numpy as np
from PIL import Image

# Con esta función normalizamos la imagen y la cambiamos de 3 a dos dimensiones
def chori(a):
    fil, col, cap = a.shape  # Extraemos sus dimensiones y las guardamos en variables separadas

    cv2.normalize(a, a, 0, 255, cv2.NORM_MINMAX)  # Normalizamos la imagen con Z-scored
    # Cambiamos las dimensiones de la imagen (de tres a dos dimensiones)
    # Order= f es para que nos muestre los ejes de las imagenes uno por uno en vez de uno por columna
    a = np.reshape(a, (fil, col * cap),order='f')
    return a

# Con esta función obtenemos las componentes de la imagen y las convertimos a diferentes formatos de imagen
def componentes(a,cmyk_image_resize):
    a1 = chori(a) #RGB
    """
    Modelo cordenadas HSV
    
    H-> angulo  equivalente R
    S-> saturacion  equivalente G
    I-> insentidas equivalente B
    
    """
    a2 = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)  # Tomamos la imagen en BGR y la convertimos a HSV
    a2 = chori(a2) #HSV

    a3 = cv2.cvtColor(a, cv2.COLOR_BGR2LAB)  # Tomamos la imagen en BGR y la convertimos a lAB
    a3 = chori(a3) #LAB

    a4=cmyk_image_resize
    a4 =chori(a4)


    return a1, a2, a3, a4  # Retornamos las imagenes separadas por componentes en cada uno de los formatos


a = cv2.imread('carro.jpg', 1)  # Leemos la imagen a la cual le aplicaremos las dos funciones anteriores
image = Image.open('carro.jpg')
cmyk_image = image.convert('CMYK')
cmyk_image = np.array(cmyk_image)


# Con esta y las tres lineas de codigo anteriores reducimos el tamaño de la imagen
# que leemos (Para nuestro caso específico era necesario pues no se mostraba en su totalidad )
a = cv2.resize(a, (300, 300),interpolation=cv2.INTER_AREA)


#Resize image CMYK
cmyk_image_resize = cv2.resize(cmyk_image, (400, 400),interpolation=cv2.INTER_AREA)

a1, a2, a3, a4 = componentes(a,cmyk_image_resize)  # Aplicamos la función componentes que a su vez utiliza la función Chori


cv2.imshow('COMPONENTES RGB', a1)  # Mostramos las imágenes
cv2.imshow('COMPONENTES HSV', a2)
cv2.imshow('COMPONENTES LAB', a3)
cv2.imshow('COMPONENTES CMYK', a4)

cv2.waitKey(0)
cv2.destroyAllWindows()

