# -*- coding: utf-8 -*-
"""
Created on 20 febrero 2020

@author: Jose Alberto Arango Sánchez
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Para salir de la ventana presionamos la tecla q


total = [] #Guardamos la suma de los pixeles del frame del movimiento
#Con el parametro 0 le indicamos que lea la camara por defecto
cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame1 = cap.read()
    #Usamos flip 1 para girar el frame horizontalmente
    frame1 = cv2.flip(frame1,1)

    ret, frame2 = cap.read()
    frame2 = cv2.flip(frame2,1)

    frame_resta = frame1 - frame2


    frame_resta[frame1 < frame2] = 0

    suma_movimiento = np.sum(frame_resta)
    total.append(suma_movimiento)

    
    # Display the resulting frame
    cv2.imshow('Camera Frame-by-Frame',frame_resta)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#Mostramos una grafica de movimiento
plt.plot(total)
plt.show()


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()