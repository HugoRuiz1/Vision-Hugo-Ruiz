#Rep. grafica de la imagen en bsase a sus pixeles
import cv2
import numpy as np
import matplotlib.pylab as plt
img_bgr=cv2.imread('drone.jpg') 
img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

img_bgr2=cv2.imread('hsv.png') 
img_rgb2=cv2.cvtColor(img_bgr2,cv2.COLOR_BGR2RGB)

hist_values=cv2.calcHist([img_bgr], channels=[0], mask=None,histSize=[256],ranges=[0,256]) #Calcula el histograma par la matriz azul, parametrode imagen, canal rgb, mascara, tamaño de histograma y rango
hist_values1=cv2.calcHist([img_bgr], channels=[1], mask=None,histSize=[256],ranges=[0,256]) 
hist_values2=cv2.calcHist([img_bgr], channels=[2], mask=None,histSize=[256],ranges=[0,256]) 
print(hist_values.shape) 
print(hist_values1.shape) 
print(hist_values2.shape) 

hist_values3=cv2.calcHist([img_bgr2], channels=[0], mask=None,histSize=[256],ranges=[0,256]) #Calcula el histograma par la matriz azul, parametrode imagen, canal rgb, mascara, tamaño de histograma y rango
hist_values4=cv2.calcHist([img_bgr2], channels=[1], mask=None,histSize=[256],ranges=[0,256]) 
hist_values5=cv2.calcHist([img_bgr2], channels=[2], mask=None,histSize=[256],ranges=[0,256]) 
print(hist_values3.shape) 
print(hist_values4.shape) 
print(hist_values5.shape) 



fig_1 = plt.figure()
# imagen original
ax1 = fig_1.add_subplot(2,2,1)
ax1.plot(hist_values)
ax1.set_title("Azul")

# recorte
ax2 = fig_1.add_subplot(2,2,2)
ax2.plot(hist_values1)
ax2.set_title("Verde")

# recorte
ax2 = fig_1.add_subplot(2,2,3)
ax2.plot(hist_values2)
ax2.set_title("Rojo")

# recorte
ax2 = fig_1.add_subplot(2,2,4)
ax2.imshow(img_rgb)
ax2.set_title("Original")



fig_2 = plt.figure()
# imagen original
ax3 = fig_2.add_subplot(2,2,1)
ax3.plot(hist_values3)
ax3.set_title("Azul")

# recorte
ax4 = fig_2.add_subplot(2,2,2)
ax4.plot(hist_values4)
ax4.set_title("Verde")

# recorte
ax5 = fig_2.add_subplot(2,2,3)
ax5.plot(hist_values5)
ax5.set_title("Rojo")

# recorte
ax6 = fig_2.add_subplot(2,2,4)
ax6.imshow(img_rgb2)
ax6.set_title("Original")

plt.show()