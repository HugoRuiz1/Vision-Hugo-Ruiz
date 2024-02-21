import cv2
import numpy as np
import matplotlib.pylab as plt
def carga_imagen(): #Funcion
    img = cv2.imread('imagen DJ RUVA.png').astype(np.float32) / 255 #Se lee como un flotante 32 bits/255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#conversion color
    return img #regresa la imagen, se regresa las 3 matrices
def despliega(img_1,img_2,img_3,img_4,img_5,img_6): #crea una variable, cada que se pase un elemento colocar parentesis
    fig=plt.figure(figsize=(10,10)) #tamaño
    ax=fig.add_subplot(2,3,1) #una sola imagen
    ax.imshow(img_1)
    ax=fig.add_subplot(2,3,2) 
    ax.imshow(img_2)     
    ax=fig.add_subplot(2,3,3) 
    ax.imshow(img_3)
    ax=fig.add_subplot(2,3,4) 
    ax.imshow(img_4)
    ax=fig.add_subplot(2,3,5) 
    ax.imshow(img_5)
    ax=fig.add_subplot(2,3,6) 
    ax.imshow(img_6)
    plt.show() #mantenga la imagen en pantalla 
imagen=carga_imagen() #carga imagen
gamma=1/50 #factor gama, factor que se eleva el pixel, se eleva a un factor determinado, eleva 1/50
eleva_un_cuarto=np.power(imagen,gamma) #genera la elevacion FILTRO 
#despliega(eleva_un_cuarto)
# Distorsión Filtro por kernel
kernel = np.ones(shape = (10,10),dtype = np.float32 )/25 #Genera la division y suma entre los pixles alrededor, matriz de 1, 10x10
distorsion = cv2.filter2D(imagen, -1,kernel) #
#despliega(distorsion)
# Distorsión por blur 
blur_distorsion=cv2.blur(imagen, ksize=(10,10)) #
#despliega(blur_distorsion) 
blur_gausiano=cv2.GaussianBlur(imagen,(5,5),50) #
#despliega(blur_gausiano)
blur_median=cv2.medianBlur(imagen,5)#Se usa sobre todo en imagenes con pixeles extra o puntos 
#despliega(blur_median)
blur_bilateral=cv2.bilateralFilter(imagen,9,75,75) #atenua las texturas, 
#despliega(blur_bilateral)
despliega(eleva_un_cuarto,distorsion,blur_distorsion,blur_gausiano,blur_median,blur_bilateral)
cv2.waitKey(0)
