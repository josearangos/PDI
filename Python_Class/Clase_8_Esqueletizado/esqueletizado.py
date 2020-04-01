import numpy as np
import cv2
from skimage.morphology import skeletonize

a = cv2.imread('figuras.bmp',0) #Leemos una imagen
cv2.imshow('figuras',a) #Mostramos la imagen que leímos

skeleton = skeletonize(a)

cv2.imshow('skeleton',skeleton) #Mostramos la imagen erosionada


cv2.waitKey(0)
cv2.destroyAllWindows()

#http://opencvpython.blogspot.com/2012/05/skeletonization-using-opencv-python.html

