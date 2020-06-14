
import cv2

camera=cv2.VideoCapture(0) #Initializing a camera object 0-default camera 1,2,3...-external cameras,
                           #or a video url, or IP address of a accessible CCTV Cam

face_clsfr=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #importing the traind DL classifier


while(True) :

    ret,frame = camera.read() #Read one frame from camera stream and store it
                                  #ret - accessible value(if the camera is accessible or not,
                                  #frame - an instant imagee captured by camera

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #coverting to grayscale image for fast processing

    faces=face_clsfr.detectMultiScale(gray) #To test the image frames using the imported classifier
                                            #detect multiple faces with a covered rectangle(giving rectangle cordinamtes)
                                            #this return cordinaes as 4 value array(x1,y1,width,height) as elements
                                            #gray imge used for detections.previews are done in color image
    for (x,y,w,h) in faces :  #loop runs for times as number of faces

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) # image,cordinated,color of frame,frame width)

        
    cv2.imshow("LIVE",frame) #showing video stream inna window called LIVE(as color)

    cv2.waitKey(1) #1 milisecond delay to slow the frame rate #make this dleay to equal camer frame rate to loop rate

    
camera.release()
    
    
