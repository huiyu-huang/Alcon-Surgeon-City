import cv2
import numpy as np
 
# can specify 0 for webcam or a video file
cap = cv2.VideoCapture(0)

width = int(cap.get(3)) #get method gets info about video metadata
height = int(cap.get(4))
fps = int(cap.get(5))
fourcc = cv2.VideoWriter_fourcc(*'MJPG') #can experiment to see which codecs work
 
out = cv2.VideoWriter('output.avi', fourcc, 20 , (width,height))
 
while(cap.isOpened()):
  ret, frame = cap.read()
 
  if ret == True: 
    
    #draws a rectangle
    frame = cv2.rectangle(frame,(int(width/2),int(height/2)),(width,height),(255,0,0),3)
    

    font = cv2.FONT_HERSHEY_SIMPLEX
    
    #adds text to video, displaying the fps of the webcam
    cv2.putText(frame,str(fps),(int(width/2),int(height/2)), font, 1,(255,255,255),2,cv2.LINE_AA)
    out.write(frame)
    
    cv2.imshow('frame',frame)
 
    #display each output frame until you want to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  else:
    break 
 
cap.release()
out.release()
 
cv2.destroyAllWindows()