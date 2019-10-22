#pip install SpeechRecognition
#pip install pydub
#pip install moviepy
#install ffmpeg, add to system path
import math

#these lines import the libraries needed
import speech_recognition as sr
from os import path
from pydub import AudioSegment
import moviepy.editor as mp


def audio_read(video):
    #this takes the first minute of the shia.mp4 video and converts it into test.mp3
    clip = mp.VideoFileClip(video)#.subclip(0,-1)


    s = math.floor(clip.duration)
    sec = math.floor(clip.duration)
    num = 0
    num2 = 0
    s2 = 10
    
##    clip2 = clip.subclip(0, s)
##    clip2.audio.write_audiofile("test" + str(num)+ ".mp3" )
##
##    num += 1
##    clip2 = clip.subclip(40, 50)
##    clip2.audio.write_audiofile("test" + str(num)+ ".mp3" )

##    s = 60
##    while s != 0:
##        #clip = mp.VideoFileClip(video)
##        #clip2 = clip.subclip(num2, s2)
##        clip2 = mp.VideoFileClip(video).subclip(num2,s2)
##        clip2.audio.write_audiofile("test" + str(num)+ ".mp3" )
##        num += 1
##        num2 += 10
##        s2 += 10
##        s -= 10
    
    ##finish up splicing video, is done
    while s != 0:
        clip2 = mp.VideoFileClip(video).subclip(num2, s2)
        clip2.audio.write_audiofile("test" + str(num)+ ".mp3" )
        num += 1
        if s > 20:
            num2 = s2
            s-=10
            s2 += 10
            print(num2)
            print(s2)
            print(s)
        else:
            num2 = s2
            s2 += (s-10)
            print(s2)
            clip2 = mp.VideoFileClip(video).subclip(num2, s2)
            clip2.audio.write_audiofile("test" + str(num)+ ".mp3" )
            s = 0

    #TODO read all these videos, lol, is done
    num2 = 0
    #this changes the mp3 to wav file
    for x in range((num+1)):


        r = sr.Recognizer()
        src = "test" + str(num2) +".mp3"
        dst = "test" + str(num2) + ".wav"
        sound = AudioSegment.from_mp3(src)
        sound.export(dst,format="wav")

        #the wav file gets recorded
        harvard = sr.AudioFile('test' + str(num2) +'.wav')
        with harvard as source:
            audio = r.record(source)

        #then it runs the google_recognizer
        try:
            print (r.recognize_google(audio))
        except:
            pass
        num2 += 1

#vid = input("What video would you like to transcribe?")
audio_read("shia.mp4")
