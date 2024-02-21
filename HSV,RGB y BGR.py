#importamos librerias
import cv2
import matplotlib.pylab as plt
#Importamos la imagen del drone en escala de grises, la dirección de la imagen se pega entre comillas dentro del paréntesis
dronegray=cv2.imread("RGB_p (1).png", 0)#Un solo canal o una sola matriz, el cero representa que esta en escala de grises
#Importamos la imagen del drone en color 
dronergb=cv2.imread("RGB_p (1).png", 1) #Tres canales o tres matrices, mandamos a llamarlas, la manda en el orden BGR y no RGB
#Importamos la imagen del drone en color
dronecolor=cv2.imread("RGB_p (1).png") #Tres canales o tres matrices
#Corrección de color de BGR a rgb
img=cv2.cvtColor(dronecolor,cv2.COLOR_BGR2RGB)
#Corrección de color de RGB a HSV
imgHSV=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
#Corrección de color de HSV a BGR
img2=cv2.cvtColor(img,cv2.COLOR_HSV2BGR)

#Extraemos los atributos principales de la imagen en escala de grises
#H = img[: , : , 0]
#S = img[: , : , 1]
#V = img[: , : , 2]
#Los 3 comandos anteriores son identicos a el siguiente comando
H,S,V = cv2.split(imgHSV) #H es el color como tal, matiz, S es la saturación y V es el valor
r,g,b = cv2.split(img)
B,G,R = cv2.split(img2)

H[:,:]=255
r[:,:]=20
R[:,:]=255

#Ploteamos los canales
fig=plt.figure()
#Canal matiz
imgre=cv2.merge((H,S,V))
ax1=fig.add_subplot(2,2,1)
ax1.imshow(imgre)
ax1.set_title("HSV")
#Canal saturación
imgr=cv2.merge((r,g,b))
ax2=fig.add_subplot(2,2,2)
ax2.imshow(imgr)
ax2.set_title("RGB")
#Canal valor
imgr2=cv2.merge((b,g,r))
ax3=fig.add_subplot(2,2,3)
ax3.imshow(imgr2)
ax3.set_title("BGR")
#Reconstrucción de imagen
ax4=fig.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("ORIGINAL")

plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)