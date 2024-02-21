import cv2

cap = cv2.VideoCapture(0) #Canal donde se muestra la cámara

winName='IP_CAM' #Ventana donde abriremos la imagen
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)

#####Función_Inicio#######
def draw_circle(event,x,y,flags,param): #corremos define, nomre de la función y elementos que vamos a pasar, evento, x y y, banderas y parámetros
    if event==cv2.EVENT_LBUTTONUP: #definimos el evento, si mi evento es igual a cuando presionemos botón izquierdo de mouse se va a generar lo de abajo
        cv2.circle(frame_2,(x,y),50,(120,255,0),-1) #crear un circulo, si tenemos el evento de arriba se va a generar el circulo. 
    pass
cv2.namedWindow(winname='IP_CAM') #esta linea y la de abajo tienen qe tener el mismo nombre
cv2.setMouseCallback('IP_CAM',draw_circle) #Pasamos imagen y funcion. Evento de los botones del mouse
#####Función_Fin##########

while(1): #Ciclo infinito
    #cap.open(url) #almacenamos lo que se este grabando
    ret,frame=cap.read() #Almacenamos dos cosas diferentes. Variable de tipo boleano que tiene valores true y false, no mas.
    #cv2.rectangle(frame,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10)
    print(frame.shape) #Tomar la medida de la imágen
    if ret: 
        
        
        #frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        frame_2=cv2.flip(frame,1) #Generamos una rotación en espejo
        cv2.imshow('IP_CAM', frame_2) #Nombre de la ventana, impagen rotada
        tecla=cv2.waitKey(1) & 0xFF  #Definimos una tecla, tecla en codigo ASCII esta en hexadecimal
    if tecla ==27: #esc es el 27 en ASCII
        break
cv2.destroyAllWindows() #Despues de esto destruye todas las ventanas

