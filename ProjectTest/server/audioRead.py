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
    f = open('test.txt','w+')
    f.close()
    
    #this takes the first minute of the shia.mp4 video and converts it into test.mp3
    clip = mp.VideoFileClip(video)#.subclip(0,-1)

    #variables for the math section
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
    try:
        while s != 0:
            clip2 = mp.VideoFileClip(video).subclip(num2, s2)
            clip2.audio.write_audiofile("test" + str(num)+ ".wav" )
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
                clip2.audio.write_audiofile("test" + str(num)+ ".wav" )
                s = 0
    except:
        print("Something is wrong with the math for the video")

    #Got the second num2 for blank video
    num2 = 0
    #this changes the mp3 to wav file
    try:
        for x in range((num+1)):


            r = sr.Recognizer()
##            src = "test" + str(num2) +".wav"
##            dst = "test" + str(num2) + ".wav"
##            sound = AudioSegment.from_mp3(src)
##            sound.export(dst,format="wav")

            #the wav file gets recorded
            harvard = sr.AudioFile('test' + str(num2) +'.wav')
            with harvard as source:
                audio = r.record(source)

            #then it runs the google_recognizer
            try:
                f = open('test.txt','a+')
                print(r.recognize_google(audio))
                f.write(r.recognize_google(audio) +"\n")
                f.close()
            except:
                pass
            num2 += 1
    except:
        print("Something wrong with the video recording")

#vid = input("What video would you like to transcribe? Remember, filename.mp4")

##try:
##    audio_read("shia.mp4")
##except:
##    print ("Exception: video not found")
