import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
 
# can specify 0 for webcam or a video file

getLabel = {
  0: "A",
  1: "B",
  2: "C",
  3: "D",
  3: "E"
}

if __name__ == "__main__":
  cap = cv2.VideoCapture("surgery1clip.mp4")
  cap.set(cv2.CAP_PROP_FRAME_WIDTH,224) #set properties of video ahead of time to correct dimensions
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT,224)
  fps = int(cap.get(5))
  sample_period = 100

  model = load_model("my_model.h5")
   
  while(cap.isOpened()):
    for i in range(sample_period): #capture every frame, or every 5 frames, based on sample_period
      ret, frame = cap.read()
      if (ret == False):
        break
   
    if ret == True: 
      
      frame = cv2.resize(frame,(224,224))
      frame = frame.astype(np.float32)
      img_tensor = np.expand_dims(frame, axis=0)
      img_tensor /= 255.

      pred = model.predict(img_tensor)

      print(pred, np.argmax(pred))
      
      cv2.imshow('frame',frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    else:
      break 
   
  cap.release()
   
  cv2.destroyAllWindows()
