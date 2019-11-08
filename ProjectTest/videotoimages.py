import cv2
import os
import moviepy.editor as mp
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#whereever you want to store your images
path = 'C:\\Users\\Chris\\Documents\\GitHub\\Alcon-Surgeon-City\\ProjectTest\\frames\\surgery1'

#whatever video you want
clip1 = VideoFileClip('surgery1right.avi').subclip(307,336)#this is the important bit
##clip2 = VideoFileClip('surgery1right.avi').subclip(31,50)
##clip3 = VideoFileClip('surgery1right.avi').subclip(111,130)
##clip4 = VideoFileClip('surgery1right.avi').subclip(131,155)
##clip = concatenate_videoclips([clip1,clip2,clip3, clip4])


clip1.write_videofile('surgery1clip.mp4')
video = cv2.VideoCapture('surgery1clip.mp4')
success,image = video.read()
count = 0
success = True
while success:
    cv2.imwrite(os.path.join(path, 'frameD2_%d.jpg'% count),image)
    success,image = video.read()
    #print ('Read a new frame: ', success)
    count += 10
print("Done!!!")
