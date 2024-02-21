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

#Extraemos los atributos principales de la imagen en escala de grises
#H = img[: , : , 0]
#S = img[: , : , 1]
#V = img[: , : , 2]
#Los 3 comandos anteriores son identicos a el siguiente comando
H,S,V = cv2.split(imgHSV) #H es el color como tal, matiz, S es la saturación y V es el valor
r,g,b = cv2.split(img)
print(H)
archivo_h=open("Matriz_h","w")
archivo_h.write('hola'%H)
archivo_h.close()

#Ploteamos los canales
fig=plt.figure()
#Canal matiz
ax1=fig.add_subplot(2,2,1)
ax1.imshow(H)
ax1.set_title("Canal h")
#Canal saturación
ax2=fig.add_subplot(2,2,2)
ax2.imshow(S)
ax2.set_title("Canal s")
#Canal valor
ax2=fig.add_subplot(2,2,3)
ax2.imshow(V)
ax2.set_title("Canal v")
#Reconstrucción de imagen
imgre=cv2.merge((H,S,V))
imgH=cv2.cvtColor(imgre,cv2.COLOR_HSV2RGB)
#Imagen original

ax4=fig.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("Original")

fig_1=plt.figure()
#Canal rojo
ax1=fig_1.add_subplot(2,2,1)
ax1.imshow(r)
ax1.set_title("Canal r")
#Canal verde
ax2=fig_1.add_subplot(2,2,2)
ax2.imshow(g)
ax2.set_title("Canal g")
#Canal azul
ax2=fig_1.add_subplot(2,2,3)
ax2.imshow(b)
ax2.set_title("Canal b")
#Reconstrucción de imagen
imgres=cv2.merge((r,g,b)) #Juntando de nuevo las matrices
#Imagen original

ax4=fig_1.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("Original")


plt.show()
#Con el teclado pasamos la imagen
cv2.waitKey(0)