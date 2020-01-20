from database import *
import os
import sys
import time
from database import upload, download

import moviepy.editor as mp
#from joshfile import uploadvideo

from flask import Flask, request, render_template, url_for, redirect
#from audioRead import audio_read
#import numpy as np
app = Flask(__name__,static_folder='static')

#value is the id
value = "1"
try:
    os.makedirs("static/"+value)
except:
    pass

#line below is for place to save video
uploads_dir = os.path.join(app.root_path, 'static')

#home page, will be the login/signup page
@app.route("/")                   
def start():
    return render_template('sendvideo.html')

#upload page, already done
@app.route("/upload")                   
def uploader():
    return render_template('sendvideo.html')

#video result page
@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    # if there is a video in the file
    if 'photo' in request.files:
        #vid is the video stream
        vid = request.files['photo']
        if vid.filename != '':
            #saves the video in the static folder as surgeryoutput.mp4
            vid.save(os.path.join(uploads_dir, value+'\surgeryoutput.mp4'))

            #shortens the video if needed
            #clip = mp.VideoFileClip(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename)).subclip(0,30)

            #joshfile, will edit the video and saves it to the static folder as surgeryoutput.mp4
            #uploadvideo(vid.filename)

            #uploads the result video to the static folder to firebase
            upload("static/"+value+"\surgeryoutput.mp4")

            #upload("test.txt")

            #downloads the video to the static folder from firebase
            download("static/surgeryoutput.mp4")

            #this is to buffer the correct video
            time.sleep(1)

    return render_template('videoresult.html')

#help page, will literally be text
@app.route("/help")                   
def help():
    return render_template('sendvideo.html')

#uploaded video, can get videos back from here
@app.route("/myvideo")                   
def myvideo():
    return render_template('sendvideo.html')


###I don't know what links are
@app.route("/links")                   
def links():
    return render_template('sendvideo.html')



if __name__ == "__main__":        
    app.run(host='0.0.0.0', debug = True)       # run the flask app, don't use debug mode for non local demo

