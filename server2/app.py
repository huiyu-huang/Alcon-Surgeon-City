from database import *
import os
import sys
from database import upload, download

import moviepy.editor as mp
from joshfile import uploadvideo

from flask import Flask, request, render_template, url_for, redirect
#from audioRead import audio_read
#import numpy as np
app = Flask(__name__,static_folder='static')

#line below is for place to save video
uploads_dir = os.path.join(app.root_path, 'static')

#home page
@app.route("/")                   
def start():
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
            vid.save(os.path.join(uploads_dir, 'surgeryoutput.mp4'))

            #shortens the video if needed
            #clip = mp.VideoFileClip(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename)).subclip(0,30)

            #joshfile, will edit the video and saves it to the static folder as surgeryoutput.mp4
            #uploadvideo(vid.filename)

            #uploads the result video to the static folder to firebase
            upload("static/surgeryoutput.mp4")

            #upload("test.txt")

            #downloads the video to the static folder from firebase
            download("static/surgeryoutput.mp4")

    return render_template('video.html')



if __name__ == "__main__":        
    app.run(host='0.0.0.0', debug = True)       # run the flask app, don't use debug mode for non local demo

