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


    clip.audio.write_audiofile("test.mp3")



    #this changes the mp3 to wav file
    r = sr.Recognizer()
    src = "test.mp3"
    dst = "test.wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst,format="wav")

    #the wav file gets recorded
    harvard = sr.AudioFile('test.wav')
    with harvard as source:
        audio = r.record(source)

    #then it runs the google_recognizer
    print (r.recognize_google(audio))

#vid = input("What video would you like to transcribe?")
audio_read("shia.mp4")
