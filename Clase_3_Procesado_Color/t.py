import cv2
import numpy as np
paisaje = cv2.imread('paisaje.jpg')
carro   =  cv2.imread('carro.jpg')
[fil,col,cap]= paisaje.shape
e=cv2.resize(carro,(400,400)) #Se  cambia el tamaño de la imagen carro 





cv2.imshow('Arroz',carro)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Hello")