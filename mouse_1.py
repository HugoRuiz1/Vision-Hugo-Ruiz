import cv2
import numpy as np
#####Función_Inicio#######
def draw_circle(event,x,y,flags,param): #corremos define, nomre de la función y elementos que vamos a pasar, evento, x y y, banderas y parámetros
    if event==cv2.EVENT_LBUTTONUP: #definimos el evento, si mi evento es igual a cuando presionemos botón izquierdo de mouse se va a generar lo de abajo
        cv2.circle(img,(x,y),50,(120,255,0),-1) #crear un circulo, si tenemos el evento de arriba se va a generar el circulo. 
    pass
cv2.namedWindow(winname='Imagen_gris') #esta linea y la de abajo tienen qe tener el mismo nombre
cv2.setMouseCallback('Imagen_gris',draw_circle) #Pasamos imagen y funcion. Evento de los botones del mouse
#####Función_Fin##########

####Mostrar_Imagenes_Inicio####
img = np.zeros((1080,1080,3),np.int8) 
while True:
    cv2.imshow('Imagen_gris',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
####Mostrar_Imagenes_Fin####

#Hacer 2 funciones boton izq, boton der, dentro de la cámara