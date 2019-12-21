from database import *
import os
import sys
from database import upload
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
    
@app.route("/")                   
def start():                      
    url = url_for('static', filename='app.js')
    return render_template('index.html', bundle = url)

@app.route("/result", methods=['POST'])              
def hello_name():              
    return render_template('result.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        vid = request.files['photo']
        
        if vid.filename != '':
            
            vid.save(os.path.join('os.path.join','static/' + vid.filename))
            #clip = mp.VideoFileClip(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/static', vid.filename)).subclip(0,30)
            #uploadvideo(vid.filename)
            #audio_read("static/surgeryoutput.mp4")
            
            upload("static/surgeryoutput.mp4")
            #upload("test.txt")
            
            
            #vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server', vid.filename))
            #vid.save(os.path.join('C:/Users/Chris/Documents/GitHub/Alcon-Surgeon-City/ProjectTest/server/templates', vid.filename))
            #upload(vid.filename)


            
    return render_template('video.html') #redirect('/') #return report



if __name__ == "__main__":        # on running python app.py
    #upload()
    app.run(host='0.0.0.0', debug = True)                     # run the flask app, don't use debug mode

