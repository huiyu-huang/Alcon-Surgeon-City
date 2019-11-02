import cv2
import os
import moviepy.editor as mp
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#whereever you want to store your images
path = 'C:\\Users\\Chris\\Documents\\GitHub\\Alcon-Surgeon-City\\ProjectTest\\frames\\surgery1'

#whatever video you want
clip = VideoFileClip('surgery1right.avi').subclip(307,335)#this is the important bit


clip.write_videofile('surgery1.mp4')
video = cv2.VideoCapture('surgery1.mp4')
success,image = video.read()
count = 0
success = True
while success:
    cv2.imwrite(os.path.join(path, 'frameL%d.jpg'% count),image)
    success,image = video.read()
    print ('Read a new frame: ', success)
    count += 10
