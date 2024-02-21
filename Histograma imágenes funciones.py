#Rep. grafica de la imagen en bsase a sus pixeles
import cv2
import numpy as np
import matplotlib.pylab as plt



##Funcion_cargar_i8magenes##
def carga_imagen1(x,y): #Funcion
    img_bgr = cv2.imread(x) #Se lee como un flotante 32 bits/255
    hist_values=cv2.calcHist([img_bgr], channels=[y], mask=None,histSize=[256],ranges=[0,256])
    return img_bgr #regresa la imagen, se regresa las 3 matrices


##Funcion_ploteo###########
def despliega1(hist_values,hist_values1,hist_values2,img_1): #crea una variable, cada que se pase un elemento colocar parentesis
    fig=plt.figure(figsize=(7,5)) #tamaño
    ax=fig.add_subplot(2,2,1) #una sola imagen
    ax.plot(hist_values)
    ax=fig.add_subplot(2,2,2) #una sola imagen
    ax.plot(hist_values1) 
    ax=fig.add_subplot(2,2,3) #una sola imagen
    ax.plot(hist_values2) 
    ax=fig.add_subplot(2,2,4) #una sola imagen
    ax.imshow(img_1) 
###########################

##Funcion_ploteo###########
def despliega2(hist_values3,hist_values4,hist_values5,img_2): #crea una variable, cada que se pase un elemento colocar parentesis
    fig2=plt.figure(figsize=(7,5)) #tamaño
    ax1=fig2.add_subplot(2,2,1) #una sola imagen
    ax1.plot(hist_values3)
    ax1=fig2.add_subplot(2,2,2) #una sola imagen
    ax1.plot(hist_values4) 
    ax1=fig2.add_subplot(2,2,3) #una sola imagen
    ax1.plot(hist_values5) 
    ax1=fig2.add_subplot(2,2,4) #una sola imagen
    ax1.imshow(img_2) 
###########################

imagen1=carga_imagen1() #carga imagen
imagen2=carga_imagen2() 

img1 = cv2.cvtColor(imagen1,cv2.COLOR_BGR2RGB)#conversion color
img2 = cv2.cvtColor(imagen2,cv2.COLOR_BGR2RGB)#conversion color


 #Calcula el histograma par la matriz azul, parametrode imagen, canal rgb, mascara, tamaño de histograma y rango
hist_values1=cv2.calcHist([imagen1], channels=[1], mask=None,histSize=[256],ranges=[0,256]) 
hist_values2=cv2.calcHist([imagen1], channels=[2], mask=None,histSize=[256],ranges=[0,256]) 
print(hist_values.shape) 
print(hist_values1.shape) 
print(hist_values2.shape) 

hist_values3=cv2.calcHist([imagen2], channels=[0], mask=None,histSize=[256],ranges=[0,256]) #Calcula el histograma par la matriz azul, parametrode imagen, canal rgb, mascara, tamaño de histograma y rango
hist_values4=cv2.calcHist([imagen2], channels=[1], mask=None,histSize=[256],ranges=[0,256]) 
hist_values5=cv2.calcHist([imagen2], channels=[2], mask=None,histSize=[256],ranges=[0,256]) 
print(hist_values3.shape) 
print(hist_values4.shape) 
print(hist_values5.shape) 

despliega1(hist_values,hist_values1,hist_values2,img1)
despliega2(hist_values3,hist_values4,hist_values5,img2)

plt.show()