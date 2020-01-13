from database import *
import os
import sys
from database import upload, download
from audioRead import audio_read
from joshfile import uploadvideo

import moviepy.editor as mp
import numpy as np
# app.py

from flask import Flask, request, render_template, url_for, redirect          
app = Flask(__name__,static_folder='static')


##@app.route('/results', methods = ['GET', 'POST'])
##def result():
##    if request.method == 'GET':
##        place = request.args.get('place', None)
##        if place:
##            return place
##        return "No place information is given"

uploads_dir = os.path.join(app.root_path, 'static')
#os.makedirs(uploads_dir)
    
@app.route("/")                   
def start():
    #print("Hello it is starting")
    #url = url_for('static', filename='app.js')
    return render_template('fireform.html')#, bundle = url)

@app.route("/result", methods=['POST'])              
def hello_name():              
    return render_template('result.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    #print("Going to vid.filename")
    
    if 'photo' in request.files:
        print("starting vid")
        vid = request.files['photo']
        print(vid)
        if vid.filename != '':
            print(vid.filename)
            #print("w32323e2e32d")
            #vid.save(vid.filename)
            vid.save(os.path.join(uploads_dir, 'surgeryoutput.mp4'))
            #clip = mp.VideoFileClip(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename)).subclip(0,30)
            uploadvideo(vid.filename)
            #audio_read("static/surgeryoutput.mp4")
            
            upload("static/surgeryoutput.mp4")

            
            #upload("test.txt")
            download("static/surgeryoutput.mp4")
            
            #vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server', vid.filename))
            #vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/templates', vid.filename))
            #upload(vid.filename)


            
    return render_template('video.html') #redirect('/') #return report



if __name__ == "__main__":        # on running python app.py
    #upload()
    app.run(host='0.0.0.0', debug = True)                     # run the flask app, don't use debug mode

