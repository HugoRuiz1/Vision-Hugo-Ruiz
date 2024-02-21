import cv2

cap = cv2.VideoCapture(0) #Canal donde se muestra la cámara

winName='IP_CAM' #Ventana donde abriremos la imagen
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)
while(1): #Ciclo infinito
    #cap.open(url) #almacenamos lo que se este grabando
    ret,frame=cap.read() #Almacenamos dos cosas diferentes. Variable de tipo boleano que tiene valores true y false, no mas.
    #cv2.rectangle(frame,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10)
    print(frame.shape) #Tomar la medida de la imágen

    if ret: 
        
        #frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        frame_2=cv2.flip(frame,1) #Generamos una rotación en espejo
        frame1=cv2.cvtColor(frame_2,cv2.COLOR_BGR2RGB) 
        r,g,b = cv2.split(frame1)
        b[:,:]=120
        imgr2=cv2.merge((r,g,b))
        #redimension=cv2.resize(rct, None, fx = 1.0, fy = 1.5) 
        #cv2.imshow(winName, frame_2) #Nombre de la ventana, impagen rotada
        cv2.imshow(winName,imgr2)
    tecla=cv2.waitKey(1) & 0xFF  #Definimos una tecla, tecla en codigo ASCII esta en hexadecimal
    if tecla ==27: #esc es el 27 en ASCII
        break
cv2.destroyAllWindows() #Despues de esto destruye todas las ventanas
#no entiendo nada y ya no se que as haer por que ya me hice bolas...... 