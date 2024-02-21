import cv2
import numpy as np
import matplotlib.pylab as plt

def carga_img1():
    img = cv2.imread('blur1.jpg').astype(np.float32) / 255 
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img 
def carga_img2():
    img1 = cv2.imread('blur2.jpg')#.astype(np.float32) / 255 
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    return img1
def despliega(img_1,img_2):
    fig=plt.figure(figsize=(10,10)) 
    ax=fig.add_subplot(2,2,1)
    ax.imshow(img_1)
    ax=fig.add_subplot(2,2,2) 
    ax.imshow(img_2)     
    plt.show()
imagen1=carga_img1()
imagen2=carga_img2() 
blur_bilateral1=cv2.bilateralFilter(imagen1,30,90,100)
blur_median=cv2.medianBlur(imagen2,23)

despliega(blur_bilateral1,blur_median)
cv2.waitKey(0)
