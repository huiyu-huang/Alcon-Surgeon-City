#pip install SpeechRecognition
#pip install pydub
#pip install moviepy
#install ffmpeg, add to system path

import speech_recognition as sr

from os import path
from pydub import AudioSegment


import moviepy.editor as mp
clip = mp.VideoFileClip("shia.mp4").subclip(0,60)
clip.audio.write_audiofile("test.mp3")


r = sr.Recognizer()
src = "test.mp3"
dst = "test.wav"

sound = AudioSegment.from_mp3(src)
sound.export(dst,format="wav")

harvard = sr.AudioFile('test.wav')
with harvard as source:
    audio = r.record(source)

print (r.recognize_google(audio))


