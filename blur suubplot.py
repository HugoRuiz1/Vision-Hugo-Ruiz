import cv2
import numpy as np
import matplotlib.pylab as plt

##Funcion_cargar_i8magenes##
def carga_imagen(): #funcion
    img = cv2.imread('imagen DJ RUVA.png').astype(np.float32) / 255 #leemos la imágen como flotante de 32 bits, y lo dividimos ente 255, para dar dimensiones diferentess
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #conversion de color
    return img #regresamos a la imágen. Por que identificamos la matriz de la imagen para regresarlas
###########################

##Funcion_ploteo###########
def despliega(img1): #pasamos la imagen img_3
    fig=plt.figure(figsize=(12,10)) #tamaño 
    ax=fig.add_subplot(3,2,1) #una sola imagen
    ax.imshow(img1) #mostramos la imagen
    plt.show() #mantener la imágen
###########################
# Distorsion
imagen=carga_imagen() 
gamma=1/50 #factor al que voy a elevar el pixel, cada pixel que tengo lo elevare a 1/50
eleva_un_cuarto=np.power(imagen,gamma) #generamos la elevación, filtro por factor de gamma
img2=despliega(eleva_un_cuarto)
# Distorsión Filtro por kernel
kernel = np.ones(shape = (10,10),dtype = np.float32 )/255 #generamos matriz de 1's, pasamos el tipo flotante
distorsion = cv2.filter2D(imagen, -1,kernel)  #pasamos la imagen, y el kernel que se acaba de crear 
#despliega(distorsion)
# Distorsión por blur 
blur_distorsion=cv2.blur(imagen, ksize=(10,10)) #pasa bajas, la dimension deja pasar hasta 10 por 10
###despliega(blur_distorsion) 
blur_gausiano=cv2.GaussianBlur(imagen,(5,5),50)
#despliega(blur_gausiano)
blur_median=cv2.medianBlur(imagen,5)#Se usa sobre todo en imagenes con pixeles extra o puntos 
#despliega(blur_median)
blur_bilateral=cv2.bilateralFilter(imagen,9,75,75)
#despliega(blur_bilateral)

cv2.waitKey(0)
