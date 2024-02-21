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
        cv2.circle(frame_2,center=(265,225),radius=30,color=(225,100,100),thickness=3) #Pasamos el frame 2 por que es el video ya rotado
        cv2.circle(frame_2,center=(365,225),radius=30,color=(225,100,100),thickness=3) #Pasamos el frame 2 por que es el video ya rotado
        rct = frame[250:573, 250:573] #Recortamos la imagen original y coloco las filas y columnas en las que queremos que se genere el recorte
        redimension=cv2.resize(rct, None, fx = 2.5, fy = 3.0) 

        fuente=cv2.FONT_ITALIC #Tipo de fuente con la que va a generar el texto
        cv2.putText(frame_2,text="Ojos detectados",org=(70,450),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=3, lineType=cv2.LINE_AA) #Escribimos lo que queramos, colocamos el punto de origen, dimension de la fuente, color, grosor y tipo de linea
        gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Conversion a gris
        cv2.imshow(winName, frame_2) #Nombre de la ventana, impagen rotada
        #cv2.imshow(winName, rct)
    tecla=cv2.waitKey(1) & 0xFF  #Definimos una tecla, tecla en codigo ASCII esta en hexadecimal
    if tecla ==27: #esc es el 27 en ASCII
        break
cv2.destroyAllWindows() #Despues de esto destruye todas las ventanas