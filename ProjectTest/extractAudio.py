###pip install sounddevice
####import sounddevice as sd
####duration = 5
####
####recording = sd.rec(int(duration*fs), samplerate=fs, channels=2)
####with open("microphone-results.wav", "wb") as f:
####    f.write(audio.get_wav_data())
##
##import speech_recognition as sr
##sample_rate = 48000
###Chunk is like a buffer. It stores 2048 samples (bytes of data) 
###here.  
###it is advisable to use powers of 2 such as 1024 or 2048 
##chunk_size = 2048
##
##r = sr.Recognizer() 

#pip install ffmpeg-python
##from os import path
##from pydub import AudioSegment
##
### files                                                                         
##src = "mlk.mp3"
##dst = "test.wav"
##
### convert wav to mp3                                                            
##sound = AudioSegment.from_mp3(src)
##sound.export(dst, format="wav")

import moviepy.editor as mp
clip = mp.VideoFileClip("shia.mp4").subclip(0,60)
clip.audio.write_audiofile("test.mp3")
