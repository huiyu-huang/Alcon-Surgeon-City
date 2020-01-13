#!/usr/bin/env python
import os
import sys
from flask import Flask, request, render_template, url_for, redirect
from database import upload, download
from audioRead import audio_read
from joshfile import uploadvideo
import moviepy.editor as mp
import numpy as np

app = Flask(__name__)
uploads_dir = os.path.join(app.root_path, 'static')

@app.route("/")                   
def start():
    ###return("Hello it is starting")
    return render_template('fireform.html')

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
            vid.save(os.path.join(uploads_dir, 'surgeryoutput.mp4'))
            
            #clip = mp.VideoFileClip(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename)).subclip(0,30)
            ####uploadvideo(vid.filename)
            ##audio_read("static/surgeryoutput.mp4")
            
            upload("static/surgeryoutput.mp4")

            
            #upload("test.txt")
            download("static/surgeryoutput.mp4")
            
            #vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server', vid.filename))
            #vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/templates', vid.filename))
            #upload(vid.filename)


            
    return render_template('video.html') #redirect('/') #return report

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True) 
