#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Importamos la imagen del drone en escala de grises
dronegray=cv2.imread("Imagen DJ RUVA.png", 0)#Un solo canal o una sola matriz, la dirección de la imagen se pega entre comillas dentro del paréntesis
#Importamos la imagen del drone en color
dronergb=cv2.imread("Imagen DJ RUVA.png", 1) #Tres canales o tres matrices, el cero representa que esta en escala de grises
#Importamos la imagen del drone en color
dronecolor=cv2.imread("Imagen DJ RUVA.png") #Tres canales o tres matrices, mandamos a llamarlas, la manda en el orden BGR y no RGB
#Extraemos los atributos principales de la imagen en escala de grises
tama=dronegray.shape
tipo= dronegray.dtype
print("Tamaño RGB | Tipo de dato |",tama, tipo  )
#Extraemos los atributos principales de la imagen RGB
tamargb=dronergb.shape
tiporgb= dronergb.dtype
print("Tamaño RGB | Tipo de dato |",tamargb, tiporgb  )
#Mostramos las imagenes desde opencv, siempre se pasa un nombre seguido de la imagen
cv2.imshow("Gray",dronegray)
cv2.imshow("RGB",dronergb)
cv2.imshow("IMG",dronecolor)
#Corrección de color para BGR a RGB 
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
#Mostramos nuestra imagen
plt.imshow(img)
plt.show()
#con el teclado cambiamos de imagen.
cv2.waitKey(0)