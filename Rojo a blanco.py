#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen blanca debido a que los valores estan en 255 y se multiplican por 1
img = 255*np.ones((255,255,3), np.uint8)
#Extraemos los canales de cada matriz de color
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
#modificamos los canales o colores de cada una de las matrices, para indicar que sean todas las filas y todas las columnas se usan los ":"
for i in range (255):
  for j in range(255):
    R[j,i]=255
    G[j,i]=i
    B[j,i]=i
#Se muestran los valores numericos, se integran las matrices
img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B
print(img)
#Se muestra la imagen
plt.imshow(img)
plt.show()

cv2.waitKey(0)