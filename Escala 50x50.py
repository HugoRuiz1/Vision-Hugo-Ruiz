#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen negra
img = np.zeros((50,50,1), np.uint8) #Dimensiones 1 matriz de 50 por 50, y es un numero entero sin signo unsigned int 8
#modificar algunos pixeles determinados, serán los qe esten entre corchetes
for i in range (51):
    img[-i,-i]=i+1
#Se muestran los valores numericos
print(img)
#Se muestra la imagen
plt.imshow(img, cmap='gray') #Pasamos los parámetros de imágen y cmap es para colocaar un color en esecífico, en este caso es escala de grises
plt.show() #Se muestra