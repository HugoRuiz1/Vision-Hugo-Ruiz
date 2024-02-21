#importamos librerias
import cv2
import matplotlib.pylab as plt
import numpy as np

#Importamos la imagen del drone en color
dronecolor=cv2.imread("ojos 2.png") 
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
B,G,R=cv2.split(img)
b_1 = np.savetxt('B_ojos_2.txt', B, delimiter =', ')   #Guardamos las matrices de bgr, cada una por separado, guardamos el canal que le digamos
G_1 = np.savetxt('G_ojos_2.txt', G, delimiter =', ')   #ponemos un delimitador que es una coma
R_1 = np.savetxt('R_ojos_2.txt', R, delimiter =', ')   #Identifficamos si a la hora de modificar los canales si lo hace o no     

cv2.waitKey(0)

