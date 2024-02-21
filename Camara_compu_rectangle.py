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
        cv2.rectangle(frame_2,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10) #Comenzamos a generar un rectanglo dentro del video
        cv2.circle(frame_2,center=(320,240),radius=20,color=(255,120,110),thickness=5) #Pasamos el frame 2 por que es el video ya rotado
        cv2.circle(frame_2,center=(50,20),radius=20,color=(255,0,255),thickness=-1) #Circulo sólido es a partir del -1
        cv2.line(frame_2,pt1=(0,0),pt2=(640,480),color=(120,120,120),thickness=5)
        fuente=cv2.FONT_ITALIC #Tipo de fuente con la que va a generar el texto
        cv2.putText(frame_2,text="Hola mundo",org=(10,240),fontFace=fuente,fontScale=2,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA) #Escribimos lo que queramos, colocamos el punto de origen, dimension de la fuente, color, grosor y tipo de linea
        gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Conversion a gris
        #cv2.imshow(winName,frame)
        rct = frame[250:573, 250:573] #Recortamos la imagen original y coloco las filas y columnas en las que queremos que se genere el recorte
        redimension=cv2.resize(rct, None, fx = 2.5, fy = 3.0) 
        cv2.imshow(winName, frame_2) #Nombre de la ventana, impagen rotada
        #cv2.imshow(winName, rct)
    tecla=cv2.waitKey(1) & 0xFF  #Definimos una tecla, tecla en codigo ASCII esta en hexadecimal
    if tecla ==27: #esc es el 27 en ASCII
        break
cv2.destroyAllWindows() #Despues de esto destruye todas las ventanas
#no entiendo nada y ya no se que as haer por que ya me hice bolas...... 