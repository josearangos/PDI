# -*- coding: utf-8 -*-
"""
Created on 18 de marzo 2020

@author: Jose Alberto Arango Sánchez
"""

import cv2
import numpy as np

paisaje = cv2.imread('paisaje.jpg')
carro   =  cv2.imread('carro.jpg')

[fil,col,cap]= paisaje.shape

cv2.imshow('Paisaje',carro)
cv2.waitKey(0)
cv2.destroyAllWindows()



















