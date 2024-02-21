#importamos librerias
import cv2
import numpy as np
import matplotlib.pylab as plt
#Crear imagen blanca debido a que los valores estan en 255 y se multiplican por 1
img = 255*np.zeros((255,255,3), np.uint8)
#Extraemos los canales de cada matriz de color
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]
#modificamos los canales o colores de cada una de las matrices, para indicar que sean todas las filas y todas las columnas se usan los ":"
for i in range (255):
  for j in range(127):
        R[j,-i]=112+(i/2)
        G[j,-i]=i-255
        B[j,-i]=112+(i/2)

#Se muestran los valores numericos, se integran las matrices
img [:,:,0]=R
img [:,:,1]=G
img [:,:,2]=B

##########################################################################################333
img2 = 255*np.zeros((255,255,3), np.uint8)
#Extraemos los canales de cada matriz de color
R = img2[:,:,0]
G = img2[:,:,1]
B = img2[:,:,2]
#modificamos los canales o colores de cada una de las matrices, para indicar que sean todas las filas y todas las columnas se usan los ":"
for i in range (255):
  for j in range(127):
        R[j,-i]=i
        G[j,-i]=i
        B[j,-i]=112+(i/2)

#Se muestran los valores numericos, se integran las matrices
img2 [:,:,0]=R
img2 [:,:,1]=G
img2 [:,:,2]=B

##########################################################################################3

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

###############################################################################

img4 = 255*np.zeros((255,255,3), np.uint8)
#Extraemos los canales de cada matriz de color
R = img4[:,:,0]
G = img4[:,:,1]
B = img4[:,:,2]
#modificamos los canales o colores de cada una de las matrices, para indicar que sean todas las filas y todas las columnas se usan los ":"
for i in range (255):
  for j in range(127):
        R[j,-i]=255
        G[j,-i]=255
        B[j,-i]=112+(i/2)

#Se muestran los valores numericos, se integran las matrices
img4 [:,:,0]=R
img4 [:,:,1]=G
img4 [:,:,2]=B

##Funcion_ploteo###########
def despliega(img3,img2,img4,img1): 
    fig=plt.figure(figsize=(10,10)) #tamaño 
    ax=fig.add_subplot(2,2,1) 
    ax.imshow(img1)
    ax.set_title("B-Mor")
    ax1=fig.add_subplot(2,2,2) 
    ax1.imshow(img2) 
    ax1.set_title("B-Azu")
    ax2=fig.add_subplot(2,2,3) 
    ax2.imshow(img3)
    ax2.set_title("B-Nar")
    ax3=fig.add_subplot(2,2,4) 
    ax3.imshow(img4) 
    ax3.set_title("B-Ama")
    plt.show() #mantener la imágen
###########################

img1=despliega(img,img2,img3,img4)

plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)