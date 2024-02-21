#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen blanca debido a que los valores estan en 255 y se multiplican por 1
img3 = 255*np.zeros((255,255,3), np.uint8)
#Extraemos los canales de cada matriz de color
R = img3[:,:,0]
G = img3[:,:,1]
B = img3[:,:,2]
#modificamos los canales o colores de cada una de las matrices, para indicar que sean todas las filas y todas las columnas se usan los ":"
for i in range (255):
  for j in range(127):
        R[j,-i]=255
        G[j,-i]=120+(i/2)
        B[j,-i]=i

#Se muestran los valores numericos, se integran las matrices
img3 [:,:,0]=R
img3 [:,:,1]=G
img3 [:,:,2]=B
print(img3)
#Se muestra la imagen
plt.imshow(img3)
plt.show()

cv2.waitKey(0)