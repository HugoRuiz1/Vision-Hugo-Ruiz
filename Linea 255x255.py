#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen negra
img = np.zeros((255,255,1), np.uint8)
for i in range (256): #El valor inicial del i es 0 y solo anotamos el valor final en este caso 254
    for j in range (255): #Hacemos que el corrimiento sea por toda la matriz
        img[j,254-i]=i #Decimos que la matriz de 0 a 255 muestre los valores de i + 1, para que se muestre desde el 0 le pongo el valor final que es 254 y le resto i

print(img)
#Se muestra la imagen
plt.imshow(img, cmap='gray') #Pasamos los parámetros de imágen y cmap es para colocaar un color en esecífico, en este caso es escala de grises
plt.show() #Se muestra