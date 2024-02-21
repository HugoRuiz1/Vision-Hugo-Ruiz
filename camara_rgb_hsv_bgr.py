import cv2

cap = cv2.VideoCapture(0) #almacena lo que se este grabando, va en 0 porque es el numero donde se encuentra la camara

winName='Rezise HSV' #nombre de la ventana 
WinName2='Rezise RGB'
WinName3='Flip BGR'
WinName4='Original'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE) #paso winName 
cv2.namedWindow(WinName2,cv2.WINDOW_AUTOSIZE) #paso winName 
cv2.namedWindow(WinName3,cv2.WINDOW_AUTOSIZE) #paso winName 
cv2.namedWindow(WinName4,cv2.WINDOW_AUTOSIZE) #paso winName 
while(1): #1, ciclos infinitos 
    #cap.open(url)
    ret,frame=cap.read() #se almacenan dos cosas diferentes, genera la lectura del video, en frame se guarda todas las imagenes del video. ret (bolean, true o false) true toma imagenes
    #cv2.rectangle(frame,pt1=(20,10),pt2=(100,200),color=(255,255,0),thickness=10)
    print(frame.shape) #tomar la medida de la imagen
    if ret: #si esta activa la camara
        
        #frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
        frame_2=cv2.flip(frame,1) #rotacion 
        frame_3=cv2.flip(frame,0) #rotacion NUEVA
        imagen_r1=cv2.resize(frame_2,(300,250))
        frame1=cv2.cvtColor(imagen_r1,cv2.COLOR_RGB2HSV) #rotacion 
        frame2=cv2.cvtColor(imagen_r1,cv2.COLOR_HSV2RGB) #rotacion 
        H,S,V = cv2.split(frame1)
        R,G,B= cv2.split(imagen_r1)
        b,g,r= cv2.split(frame_3)
        #modificamos loS canales RGB

        frame3=cv2.cvtColor(frame_3,cv2.COLOR_RGB2BGR) #rotacion
        H[:,:]=255
        R[:,:]=20
        r[:,:]=255
        
        imgr=cv2.merge((H,S,V))
        imgr2=cv2.merge((R,G,B))
        imgr3=cv2.merge((b,g,r))
        frame4=cv2.cvtColor(imgr,cv2.COLOR_HSV2RGB) #rotacion 
        frame6=cv2.cvtColor(imgr3,cv2.COLOR_BGR2RGB) #rotacion

        fuente=cv2.FONT_ITALIC #tipo de fuente que se genera
        #escribir lo que se quiera, org -- punto de origen, tipo de linea
        cv2.putText(frame4,text="Rezise HSV",org=(10,240),fontFace=fuente,fontScale=1,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(imgr2,text="Rezise RGB",org=(10,240),fontFace=fuente,fontScale=1,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(frame6,text="Flip BGR",org=(10,240),fontFace=fuente,fontScale=1,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        cv2.putText(frame,text="Original",org=(10,240),fontFace=fuente,fontScale=1,color=(230,250,255),thickness=1, lineType=cv2.LINE_AA)
        #cv2.imshow(winName,frame)
        rct = frame[250:573, 250:573] #generar un recorte recorte imangen original, coloca filas y columnas 
        redimension=cv2.resize(rct, None, fx = 2.5, fy = 3.0) #
        
        cv2.imshow(winName, frame4) #nombre de la camara, imagen rotada
        cv2.imshow(WinName2, imgr2) #nombre de la camara, imagen rotada
        cv2.imshow(WinName3, frame6) #nombre de la camara, imagen rotada
        cv2.imshow(WinName4, frame) #nombre de la camara, imagen rotada
        #cv2.imshow(winName, rct)
    tecla=cv2.waitKey(1) & 0xFF #define una tecla convertido en exadecimal
    if tecla ==27: #esc es el 27 en ASCII
        break
cv2.destroyAllWindows()