import cv2
import os
import moviepy.editor as mp
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

clip1 = VideoFileClip('surgery2right.avi').subclip(4,23)#this is the important bit
clip2 = VideoFileClip('surgery2right.avi').subclip(39,55)
clip3 = VideoFileClip('surgery2right.avi').subclip(60,76)
clip = concatenate_videoclips([clip1,clip2,clip3])


clip.write_videofile('surgery2clip.mp4')
