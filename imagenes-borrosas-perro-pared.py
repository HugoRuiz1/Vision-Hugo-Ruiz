import cv2
import numpy as np
import matplotlib.pylab as plt

##Funcion_cargar_i8magenes##
def carga_imagen1(): #Funcion
    img = cv2.imread('blur1.jpg').astype(np.float32) / 255 #Se lee como un flotante 32 bits/255
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#conversion color
    return img #regresa la imagen, se regresa las 3 matrices
###########################
def carga_imagen2(): #Funcion
    img1 = cv2.imread('blur2.jpg').astype(np.float32) / 255 #Se lee como un flotante 32 bits/255
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)#conversion color
    return img1 #regresa la imagen, se regresa las 3 matrices
###########################
##Funcion_ploteo###########
def despliega(img_1,img_2): #crea una variable, cada que se pase un elemento colocar parentesis
    fig=plt.figure(figsize=(10,10)) #tamaño
    ax=fig.add_subplot(2,2,1) #una sola imagen
    ax.imshow(img_1)
    ax=fig.add_subplot(2,2,2) 
    ax.imshow(img_2)     
    plt.show() #mantenga la imagen en pantalla 
###########################
# Distorsion
imagen1=carga_imagen1() #carga imagen
imagen2=carga_imagen2() 

#blur_median=cv2.medianBlur(imagen1,5)#Se usa sobre todo en imagenes con pixeles extra o puntos 
#despliega(blur_median)
blur_bilateral2=cv2.bilateralFilter(imagen2,15,75,75) #atenua las texturas, 
blur_bilateral=cv2.bilateralFilter(imagen1,10,75,75) #atenua las texturas, 
blur_median=cv2.medianBlur(blur_bilateral,5)
blur_median2=cv2.medianBlur(blur_bilateral2,5)
#despliega(blur_bilateral)
despliega(blur_median2,blur_median)
cv2.waitKey(0)
