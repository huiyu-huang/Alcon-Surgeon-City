import cv2
import os

#whereever you want to store your images
path = 'C:\\Users\\Chris\\Documents\\GitHub\\Alcon-Surgeon-City\\ProjectTest\\frames'

#whatever video you want
video = cv2.VideoCapture('shia.mp4')
success,image = video.read()
count = 0
success = True
while success:
    cv2.imwrite(os.path.join(path, 'frame%d.jpg'% count),image)
    success,image = video.read()
    print ('Read a new frame: ', success)
    count += 1
