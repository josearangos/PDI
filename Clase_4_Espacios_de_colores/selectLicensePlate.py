import cv2
import numpy as np
from PIL import Image


# la mejor capa del formato del color  CMYK
image = Image.open('carro.jpg')
#Convertimos la imagene de RGB a CMYK
cmyk_image = image.convert('CMYK')
#Convertimos de typo Image a numpyarray
cmyk_image = np.array(cmyk_image)

cmyk_image_resize = cv2.resize(cmyk_image[:,:,0:3], (700, 700),interpolation=cv2.INTER_AREA)

#la mejor capa del formato del color  CMYK
y = cmyk_image_resize[:,:,0]

#normalizamos las mejores capas por formato de color



print(y.shape)

cv2.imshow('CMYK', y)


cv2.waitKey(0)
cv2.destroyAllWindows()